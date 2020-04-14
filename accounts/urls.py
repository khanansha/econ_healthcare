from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('rest_password/', views.rest_password, name='rest_password'),
    path('resetpass/', views.resetpass, name='resetpass'),
]
