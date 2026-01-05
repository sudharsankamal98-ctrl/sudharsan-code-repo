from django.urls import path

from app04 import views

urlpatterns = [
    path('', views.app04_index),
]