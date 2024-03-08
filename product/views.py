from django.shortcuts import render
from accounts.models import User
# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Category,Discount,Comment,ProductFeatureValue,ProductFeature,News
from .serializers import CategorySerializer,ProductSerializer,DiscountSerializer,CommentSerializer,NewsSerializer,ProductFeatureSerializer,ProductFeatureValueSerializer,UserSerializer
from rest_framework import status
from rest_framework import filters
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page

from rest_framework import generics

from django.shortcuts import get_object_or_404


#show all category
@api_view(['GET'])
@cache_page(60*15)
def get_details(request):
    category = Category.objects.filter(is_sub=False)
    serializer = CategorySerializer(category, many=True)
    return Response({'category': serializer.data})

#show all subcategory
@api_view(['GET'])
@cache_page(60*15)
def get_details_sub(request,slug):
    subcategory = Category.objects.get(slug=slug)
    subcategories = Category.objects.filter(parent_category=subcategory)
    serializer = CategorySerializer(subcategories, many=True)
    return Response({'subcategory': serializer.data})

#show all products
@api_view(['GET'])
@cache_page(60*15)
def get_product(request,slug):
    category_parent = Category.objects.get(slug=slug)
    product = Product.objects.filter(category_id = category_parent)
    serializer = ProductSerializer(product,many=True)
    return Response({'products':serializer.data})
    
    
#show detail product
@api_view(['GET'])
@cache_page(60*15)
def get_detail_product(request,slug):
    product = Product.objects.get(slug=slug)
    serializer = ProductSerializer(instance=product)
    features = ProductFeature.objects.filter(product=product)
    features_serializer = ProductFeatureSerializer(instance=features, many=True)
    feature_values = ProductFeatureValue.objects.filter(product=product)
    feature_value_serializer = ProductFeatureValueSerializer(instance=feature_values, many=True)
    comments = Comment.objects.filter(product_id=product)
    comment_serializer = CommentSerializer(instance=comments, many=True)
    discount_serializer = DiscountSerializer(instance=product.discount_id) 
    response_data = {
    "features":features_serializer.data,
    "feature_values":feature_value_serializer.data,
    "product":serializer.data,
    "discounts":discount_serializer.data,
    "comments":comment_serializer.data,
    }
    return Response(data=response_data, status=status.HTTP_200_OK)    
    
    
    
#show all discount 
@api_view(['GET'])
@cache_page(60*15)
def get_discount(request):
    discount = Discount.objects.all()
    serializer = DiscountSerializer(discount,many=True)
    return Response({'discount':serializer.data})

#show all products comment
@api_view(['GET'])
@cache_page(60*15)
def get_comment(request,slug):
    product_parent = Product.objects.get(slug=slug)
    comment = Comment.objects.filter(product_id = product_parent)
    serializer = CommentSerializer(comment,many=True)
    return Response({'comment':serializer.data})


#show all product feature
@api_view(['GET'])
@cache_page(60*15)
def get_productfeature(request,slug):
    product_parent = Product.objects.get(slug=slug)
    product_feature = ProductFeatureValue.objects.filter(product= product_parent)
    serializer = ProductFeatureValueSerializer(product_feature,many=True)
    return Response({'product_feature':serializer.data})

#show all news
@api_view(['GET'])
@cache_page(60*15)
def get_news(request):
    news = News.objects.all()
    serializer =NewsSerializer(news,many=True)
    return Response({'news':serializer.data})

#search product by name
class SearchAPIView(generics.ListCreateAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
  
#show all users
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer =UserSerializer(users,many=True)
    return Response({'user':serializer.data})

  
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
    return render(request,'product_list.html',context={})

def comment(request,slug):
    return render(request , 'comment.html' ,context={})

# def product_list(request,slug):
#     product_list = Product.objects.all()
#     page = request.GET.get('page', 1)

#     paginator = Paginator(product_list, 10)
#     try:
#         users = paginator.page(page)
#     except PageNotAnInteger:
#         users = paginator.page(1)
#     except EmptyPage:
#         users = paginator.page(paginator.num_pages)
#     return render(request , 'product_list.html' ,context={'users': users})

def product_detail(request,slug):
    return render(request , 'product_details.html' ,context={})





