from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Home page view using a template"""
    return render(request, 'home.html')

def about(request):
    """About page view using a template"""
    return render(request, 'about.html')

def contact(request):
    """Contact page view using a template"""
    return render(request, 'contact.html')

def services(request):
    """Services page view"""
    return render(request, 'services.html')

def portfolio(request):
    """Portfolio page view"""
    return render(request, 'portfolio.html')

def blog(request):
    """Blog page view"""
    return render(request, 'blog.html')

# Keeping old views for backward compatibility
def home_template(request):
    """Home page view using a template"""
    return render(request, 'home.html')

def about_template(request):
    """About page view using a template"""
    return render(request, 'about.html')

def contact_template(request):
    """Contact page view using a template"""
    return render(request, 'contact.html')