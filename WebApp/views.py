from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Module, Registration
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

def list_modules(request):
    modules = Module.objects.all()
    return render(request, 'WebApp/ListOfModules.html', {'modules': modules})

@login_required
def registermod(request, module_id):
    module = Module.objects.get(id=module_id)
    student = request.user.student
    registration = Registration(student=student, module=module)
    registration.save()
    return redirect('list_modules')

@login_required
def unregister(request, registration_id):
    registration = Registration.objects.get(id=registration_id)
    registration.delete()
    return redirect('list_modules')