from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    return HttpResponse("Hello, this is the contact page! You imported it from recipes/views.py")

def about(request):
    return HttpResponse("Hello, this is the about page! You imported it from recipes/views.py")