from django.urls import path

from . import views

urlpatterns = [

    path('profile/', views.profile, name='profile'),
    path('covid/', views.covid, name='covid'),
    path('home/', views.home, name='home'),
    path('managepro/', views.managepro, name='managepro'),
    path('dial/', views.dial, name='dial'),
    path('doctor_spcl/', views.doctor_spcl, name='doctor_spcl'),
    path('doctor_search/', views.doctor_search, name='doctor_search'),
    path('doctor_details/', views.doctor_details, name='doctor_details'),
]
