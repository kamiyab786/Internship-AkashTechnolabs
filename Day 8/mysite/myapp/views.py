from django.shortcuts import render

# Create your views here.

def travel(request):
    return render(request,'travel.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
