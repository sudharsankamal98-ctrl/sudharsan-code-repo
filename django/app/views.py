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

def running_index(request):
    """Running template index page"""
    return render(request, 'running/index.html')

def running_about(request):
    """Running template about page"""
    return render(request, 'running/about.html')

def running_blog(request):
    """Running template blog page"""
    return render(request, 'running/blog.html')

def running_blog_single_post(request):
    """Running template blog single post page"""
    return render(request, 'running/blogsinglepost.html')

def running_contact(request):
    """Running template contact page"""
    return render(request, 'running/contact.html')

def running_running(request):
    """Running template running page"""
    return render(request, 'running/running.html')

def running_running_single_post(request):
    """Running template running single post page"""
    return render(request, 'running/runningsinglepost.html')