from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Category
from .serializers import CategorySerializer

@api_view(['GET'])
def get_details(request):
    product = Product.objects.all()
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response({'category': serializer.data})



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