from django import forms
from django.shortcuts import get_object_or_404, render




# Create your views here.

def home(request):
   

    return render(request, 'WebApp/home.html', {'title': 'Homepage'}) 

def contact(request):

    return render(request, 'WebApp/contact.html', {'title': 'Contact Us'})

def about(request):

    return render(request, 'WebApp/about.html', {'title': 'About Us'})