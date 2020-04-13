from django.urls import path

from . import views

urlpatterns = [

    path('profile/', views.profile, name='profile'),
    path('covid/', views.covid, name='covid'),
    path('home/', views.home, name='home'),
]