from django.shortcuts import render,get_list_or_404,redirect
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.views import APIView
from product.models import Product
from .models import Order,OrderItem,Coupon
from .serializers import CartItemSerializer,CartSerializer,CouponSerializer,OrderSerializer,OrderItemSerializer
from django.views import View
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db.models import QuerySet
import json

def cart(request):
    return render(request,'cart.html',context={})


def detail_cart(request):
    return render(request,'detail_cart.html',context={})

    
class ShowCart(APIView):
    def get(self, request):
        cart = CartAdd(request)
        cart_items = list(cart)
        total_price = cart.get_total_price()
        for item in cart_items:
            product = serialize('json', [item['product']], fields=('name', 'price', 'slug'))
            item['product'] = {
                'fields': json.loads(product)[0]['fields'],
                'slug': item['product'].slug,
            }
        data = {
            'cart': cart_items,
            'total_price': total_price
        }
        
        return Response(data)
    
# class CartAdd:
#     def __init__(self,request) -> None:
#         self.session=request.session
#         cart = self.session.get(CART_SESSION_ID)
#         if not cart:
#             cart=self.session[CART_SESSION_ID] = {}
#         self.cart=cart
        
#     def __iter__(self):
#         product_ids=self.cart.keys()
#         products=Product.objects.filter(id__in=product_ids)
#         cart=self.cart.copy()
#         for product in products:
#             cart[str(product.id)]['product']=product.name
        
        
#     def add(self,product,quantity):
#         product_id=str(product.id)
#         if product_id not in self.cart:
#             self.cart[product_id]={'qsuantity':0,'price':str(product.price)}
#         else:
#             self.cart[product_id]['quantity']+=quantity
#         self.save()
        
#     def save(self):    
#         self.session.modified=True
CART_SESSION_ID = 'cart'
class CartAdd:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart
        
    def __iter__(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        cart=self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']=product
        for item in cart.values():
            item['total_price']=int(item['price'])*item['quantity']
            yield item
            
             
    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True    
        
    def get_total_price(self):
        return sum(int(item['price'])*item['quantity'] for item in self.cart.values())
    
    def remove(self,product):
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
        
        
class Cart_Add(APIView):
    def post(self, request, slug):
        cart = CartAdd(request)
        data=request.POST
        quantity=data["myInput"]
        print(quantity)
        try:
            queryset = Product.objects.get(slug=slug)
            cart.add(queryset,int(quantity))
        except Product.DoesNotExist:
            return redirect('cart')  
        print(request.session.get(CART_SESSION_ID))
        return redirect('cart') 


class CartRemoveApi(APIView):
    def get(self,request,slug):
        cart=CartAdd(request)
        queryset = Product.objects.get(slug=slug)
        cart.remove(queryset)
        return redirect('cart') 


class OrderDetail(APIView):
    def get(self,request,order_id):
        queryset=Order.objects.get(id=order_id)
        serializer=OrderSerializer(queryset)
        return Response({'queryset':serializer.data})

class OrderCreate(APIView):
    def get(self,request):
        cart=CartAdd(request)
        order=Order.objects.create()
        for item in cart:
            OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])

        return redirect(order.id)




# @api_view(['POST'])
# def cart_add(request,slug):
#     cart=CartAdd
#     product = Product.objects.filter(slug=slug)
#     serializer = CategorySerializer(category, many=True)
#     return Response({'category': serializer.data})


