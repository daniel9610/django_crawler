"""crawler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from users import views as users_views
from place import views as places_views
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import logout
from django.conf import settings

urlpatterns = [
    path('site_detail/', include('place.urls')),
    path('home/', places_views.HomeView.as_view(), name ='home'),
    path('sites/', places_views.ScrapedPagesView.index, name ='sites'),  
    path('admin/', admin.site.urls, name='admin'),
    path('users/login', users_views.login_view, name='login'),
    path('users/signup', users_views.signup_view, name='signup'),
    path('users/logout', users_views.logout_view, name='logout'),

    #social login
    path('', include('social_django.urls', namespace='social')),
]
