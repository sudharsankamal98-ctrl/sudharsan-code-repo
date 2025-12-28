from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """Basic home page view"""
    return HttpResponse("Hello, World! Welcome to Django!")

def about(request):
    """Basic about page view"""
    return HttpResponse("This is the about page of our Django application.")

def home_template(request):
    """Home page view using a template"""
    return render(request, 'app/home.html')

def about_template(request):
    """About page view using a template"""
    return render(request, 'app/about.html')
def contact_template(request):
    """Contact page view using a template"""
    return render(request, 'app/contact.html')