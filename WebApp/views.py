from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

def home(request):
    courses = Group.objects.all()
    return render(request, 'WebApp/home.html', {'courses': courses})

def about_us(request):
    return render(request, 'WebApp/about.html')

def contact(request):
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # TODO: Send email using the provided information
        return redirect('contact')
    else:
        return render(request, 'WebApp/contact.html')
