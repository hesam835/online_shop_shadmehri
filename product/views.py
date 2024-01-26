from django.shortcuts import render

# Create your views here.

def about_us(request):
    return render(request , 'about.html' , context={})

def contact(request):
    return render(request , 'contact.html' ,context={})

def cycle(request):
    return render(request , 'cycle.html' ,context={})

def index(request):
    return render(request , 'index.html' ,context={})

def news(request):
    return render(request , 'news.html' ,context={})