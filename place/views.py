from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup
from .templates.places.forms import SiteForm
from django.urls import reverse_lazy
import urllib.request
from django.views.generic import TemplateView, CreateView, DetailView
from place.models import Place
from content.models import Content
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils.html import escape
import json


# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    redirect_field_name = 'home'
    template_name = 'places/home.html'
   

    def get(self, request):
        form = SiteForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = SiteForm(request.POST)
        if form.is_valid():
            max_pages = 3
            counter = 0
            results = []
            domain = form.cleaned_data['domain']
            site_url = form.cleaned_data['url']
            filt_by = form.cleaned_data['filt_by']
            css_class = form.cleaned_data['css_class']
            for i in range(1, max_pages):
            
                if i > 1:
                    url = "%spage/%d/" % (site_url, i)
                else:
                    url = site_url
                redditFile = urllib.request.urlopen(url)
                statusCode = redditFile.getcode()
                print (statusCode)
                if statusCode == 200:    
                    redditHtml = redditFile.read()
                    soup = BeautifulSoup(redditHtml)
                    title = soup.find('title').getText()
                    redditAll = soup.find_all(filt_by, {'class':css_class})
                    
                    for entrada in redditAll:
                        counter += 1
                        result = entrada.get_text(strip=True)
                        print (counter, result)
                        results.append(result) 
                    json_results = json.dumps(results) #convert list to json
                    print (json_results) 

                    web_html = Place(title=title, domain=domain, user= request.user)
                    web_html.save()
                    place_id = Place.objects.get(id=web_html.id)
                    web_content = Content(site_id=place_id, html = results, qualification="chevere", secondary_url=url)
                    web_content.save()
        
                    args = {'form':form, 'site_title':title, 'site_url':json_results}  
                else:
                    break
        return render(request, self.template_name, args)
    
class ScrapedPagesView(LoginRequiredMixin):
    login_url = 'login'
    redirect_field_name = 'places'
    @login_required
    def index(request):
        cr_sites = Place.objects.all()
        context = {'cr_sites':cr_sites}
        # print(cr_sites.__dict__)
        return render(request, 'places/index.html', context)

class PlaceDetailView(LoginRequiredMixin ,DetailView):
    template_name = 'places/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    queryset = Place.objects.all()

