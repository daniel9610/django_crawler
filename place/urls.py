from django.urls import path
from django.conf.urls import url
# from place.views import HomeView, CreatePlaceView

from . import views

urlpatterns = [
    # path('', views.HomeView, name='home'),
    # url(r'^$', HomeView.as_view(), name ='home'),
    # path('users/logout', users_views.logout_view, name='logout'),
    # path('', CreatePlaceView.as_view(), name='create'),
    path(
        route='<str:id>/',
        view=views.PlaceDetailView.as_view(),
        name='detail'
    ),
]
