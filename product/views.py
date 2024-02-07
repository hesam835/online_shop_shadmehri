from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Category
from .serializers import CategorySerializer,ProductSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def get_details(request):
    category = Category.objects.filter(is_sub=False)
    serializer = CategorySerializer(category, many=True)
    return Response({'category': serializer.data})


@api_view(['GET'])
def get_details_sub(request,slug):
    subcategory = Category.objects.get(slug=slug)
    subcategories = Category.objects.filter(parent_category=subcategory)
    serializer = CategorySerializer(subcategories, many=True)
    return Response({'subcategory': serializer.data})

@api_view(['GET'])
def get_product(request,slug):
    category_parent = Category.objects.get(slug=slug)
    product = Product.objects.filter(category_id = category_parent)
    serializer = ProductSerializer(product,many=True)
    return Response({'products':serializer.data})
    
    
    
def about_us(request):
    return render(request , 'about.html' , context={})

def contact(request):
    return render(request , 'contact.html' ,context={})

def index(request):
    return render(request , 'index.html' ,context={})

def cycle(request):
    return render(request , 'cycle.html' ,context={})

def news(request):
    return render(request , 'news.html' ,context={})

def subcategory(request,slug):
    return render(request , 'subcategory.html' ,context={})

def product_list(request,slug):
    return render(request , 'product_list.html' ,context={})

def product_detail(request):
    return render(request , 'product_detail.html' ,context={})