from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home-template/', views.home_template, name='home_template'),
    path('about-template/', views.about_template, name='about_template'),
    path('contact-template/', views.contact_template, name='contact_template'),
    path('running/', views.running_index, name='running_index'),
    path('running/about/', views.running_about, name='running_about'),
    path('running/blog/', views.running_blog, name='running_blog'),
    path('running/blog/post/', views.running_blog_single_post, name='running_blog_single_post'),
    path('running/contact/', views.running_contact, name='running_contact'),
    path('running/running/', views.running_running, name='running_running'),
    path('running/running/post/', views.running_running_single_post, name='running_running_single_post'),
]