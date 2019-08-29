from django import forms
from place.models import Place

class SiteForm(forms.Form):

    domain = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter site domain'}), label="Site Domain")
    url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter site url'}), label="Site URL")
    filt_by = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter filter'}), label="filter by")
    css_class = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter css class'}), label="Css Class")
    class Meta:
        model = Place
        fields = ('title', 'url', 'user')
        widgets = {
            'domain':forms.TextInput(attrs={'class':'form-control'}),
            'url':forms.TextInput(attrs={'class':'form-control'}),
            'filt_by':forms.TextInput(attrs={'class':'form-control'}),
            'css_class':forms.TextInput(attrs={'class':'form-control'})
        }

        


    