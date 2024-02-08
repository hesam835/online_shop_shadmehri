from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Category,Discount,Comment
from .serializers import CategorySerializer,ProductSerializer,DiscountSerializer,CommentSerializer,NewsSerializer
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
    
    
@api_view(['GET'])
def get_detail_product(request,slug):
    product = get_object_or_404(Product, slug=slug)
    serializer = ProductSerializer(instance=product)
    # features = ProductFeature.objects.filter(products=product)
    # features_serializer = ProductFeatureSerializer(instance=features, many=True)
    # feature_values = ProductFeatureValue.objects.filter(product=product)
    # feature_value_serializer = ProductFeatureValueSerializer(instance=feature_values, many=True)
    comments = Comment.objects.filter(product=product)
    comment_serializer = CommentSerializer(instance=comments, many=True)
    discount_serializer = DiscountSerializer(instance=product.discount) 
    response_data = {
    # "features":features_serializer.data,
    # "feature_values":feature_value_serializer.data,
    "product":serializer.data,
    "discounts":discount_serializer.data,
    "comments":comment_serializer.data,
    }
    return Response(data=response_data, status=status.HTTP_200_OK)    
    
    
    
    
@api_view(['GET'])
def get_discount(request,slug):
    category_parent = Category.objects.get(slug=slug)
    discount = Discount.objects.filter(category_id = category_parent)
    serializer = DiscountSerializer(discount,many=True)
    return Response({'discount':serializer.data})

@api_view(['GET'])
def get_comment(request,slug):
    product_parent = Product.objects.get(slug=slug)
    comment = Comment.objects.filter(product_id = product_parent)
    serializer = CommentSerializer(comment,many=True)
    return Response({'comment':serializer.data})


@api_view(['GET'])
def get_productfeature(request,slug):
    product_parent = Product.objects.get(slug=slug)
    product_feature = ProductFeature.objects.filter(product_id = product_parent)
    serializer = ProductFeatureSerializer(product_feature,many=True)
    return Response({'product_feature':serializer.data})

@api_view(['GET'])
def get_news(request,slug):
    news = ProductFeature.objects.all()
    serializer =NewsSerializer(news,many=True)
    return Response({'news':serializer.data})

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

def product_detail(request,slug):
    return render(request , 'product_details.html' ,context={})





