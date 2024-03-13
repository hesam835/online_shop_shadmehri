from django.shortcuts import render
from accounts.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, Discount, Comment, ProductFeatureValue, ProductFeature, News
from .serializers import CategorySerializer, ProductSerializer, DiscountSerializer, CommentSerializer, NewsSerializer, ProductFeatureSerializer, ProductFeatureValueSerializer, UserSerializer
from rest_framework import status
from rest_framework import filters
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


@api_view(['GET'])
@cache_page(60*15)
def get_details(request):
    """
    Retrieve all categories.

    Returns:
        Response: JSON response containing all categories.
    """
    category = Category.objects.filter(is_sub=False)
    serializer = CategorySerializer(category, many=True)
    return Response({'category': serializer.data})

@api_view(['GET'])
@cache_page(60*15)
def get_details_sub(request, slug):
    """
    Retrieve all subcategories for a given category.

    Args:
        request: HTTP request object.
        slug (str): Slug of the parent category.

    Returns:
        Response: JSON response containing all subcategories.
    """
    subcategory = Category.objects.get(slug=slug)
    subcategories = Category.objects.filter(parent_category=subcategory)
    serializer = CategorySerializer(subcategories, many=True)
    return Response({'subcategory': serializer.data})

@api_view(['GET'])
@cache_page(60*15)
def get_product(request, slug):
    """
    Retrieve all products for a given category.

    Args:
        request: HTTP request object.
        slug (str): Slug of the category.

    Returns:
        Response: JSON response containing all products.
    """
    category_parent = Category.objects.get(slug=slug)
    product = Product.objects.filter(category_id=category_parent)
    serializer = ProductSerializer(product, many=True)
    return Response({'products': serializer.data})

@api_view(['GET'])
@cache_page(60*15)
def get_detail_product(request, slug):
    """
    Retrieve details of a specific product.

    Args:
        request: HTTP request object.
        slug (str): Slug of the product.

    Returns:
        Response: JSON response containing product details.
    """
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
        "features": features_serializer.data,
        "feature_values": feature_value_serializer.data,
        "product": serializer.data,
        "discounts": discount_serializer.data,
        "comments": comment_serializer.data,
    }
    return Response(data=response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_discount(request):
    """
    Retrieve all discounts.

    Returns:
        Response: JSON response containing all discounts.
    """
    discount = Discount.objects.all()
    serializer = DiscountSerializer(discount, many=True)
    return Response({'discount': serializer.data})

class CommentAPIView(APIView):
    serializer_class = CommentSerializer
    def get(self, request, slug):
        try:
            product_parent = Product.objects.get(slug=slug)
            comments = Comment.objects.filter(product_id=product_parent)
            serializer = CommentSerializer(comments, many=True)
            return Response({'comment': serializer.data}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    def post(self, request, slug):
        data = request.data
        product = Product.objects.get(slug=slug)
        Comment.objects.create(text_message=data["text_message"], user_id=request.user, product_id=product)
        return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@cache_page(60*15)
def get_productfeature(request, slug):
    """
    Retrieve all features for a specific product.

    Args:
        request: HTTP request object.
        slug (str): Slug of the product.

    Returns:
        Response: JSON response containing all product features.
    """
    product_parent = Product.objects.get(slug=slug)
    product_feature = ProductFeatureValue.objects.filter(product=product_parent)
    serializer = ProductFeatureValueSerializer(product_feature, many=True)
    return Response({'product_feature': serializer.data})

@api_view(['GET'])
@cache_page(60*15)
def get_news(request):
    """
    Retrieve all news items.

    Returns:
        Response: JSON response containing all news items.
    """
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response({'news': serializer.data})


class SearchAPIView(generics.ListCreateAPIView):
    """
    Search products by name.

    Attributes:
        search_fields (list): List of fields to search.
        filter_backends (tuple): Tuple of filter backends.
        queryset (QuerySet): Queryset containing all products.
        serializer_class (Serializer): Serializer class for products.
    """
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



@api_view(['GET'])
def get_users(request):
    """
    Retrieve all users.

    Returns:
        Response: JSON response containing all users.
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({'user': serializer.data})

def about_us(request):
    """Render the about us page."""
    return render(request, 'about.html', context={})

def contact(request):
    """Render the contact page."""
    return render(request, 'contact.html', context={})

def index(request):
    """Render the index page."""
    return render(request, 'index.html', context={})

def cycle(request):
    """Render the cycle page."""
    return render(request, 'cycle.html', context={})

def news(request):
    """Render the news page."""
    return render(request, 'news.html', context={})

def subcategory(request, slug):
    """Render the subcategory page."""
    return render(request, 'subcategory.html', context={})

def product_list(request, slug):
    """Render the product list page."""
    return render(request, 'product_list.html', context={})

def comment(request,slug):
    """Render the comment page."""
    return render(request, 'comment.html', context={})

def product_detail(request, slug):
    """Render the product detail page."""
    return render(request, 'product_details.html', context={})
