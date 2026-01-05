from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('aboutpage', views.about),
    path('contact', views.contact),
    path('services', views.services),
    path('portfolio', views.portfolio),
    path('blog', views.blog)]