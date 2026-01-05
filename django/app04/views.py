from django.shortcuts import render

# Create your views here.
def app04_index(request):
    return render(request, 'app04/index.html')