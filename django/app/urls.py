from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home-template/', views.home_template, name='home_template'),
    path('about-template/', views.about_template, name='about_template'),
    path('contact-template/', views.contact_template, name='contact_template'),
       
]