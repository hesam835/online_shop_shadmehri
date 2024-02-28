from django.shortcuts import render,get_list_or_404,redirect
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from product.models import Product
from .models import Order,OrderItem,Coupon
from .serializers import CartItemSerializer,CartSerializer,CouponSerializer,OrderSerializer,OrderItemSerializer,AddressSerializer
from django.views import View
from django.conf import settings
import requests
import json
from rest_framework.response import Response
from .permissions import IsOrderOwner
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db.models import QuerySet
from rest_framework import status
from django.contrib.auth.models import AnonymousUser

import json

def cart(request):
    return render(request,'cart.html',context={})


def detail_cart(request,order_id):
    return render(request,'detail_cart.html',context={})


def order_history(request):
    return render(request,'order_history.html',context={})
    
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
            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())         
    
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
            
    def clear(self):
        del self.session[CART_SESSION_ID]
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
        print("==============================")
        print(request.user)
        cart=CartAdd(request)
        total_price=cart.get_total_price()
        order=Order.objects.create(user=request.user,total_price=total_price)
        for item in cart:
            OrderItem.objects.create(order=order,product=item['product'],quantity=item['quantity'])
        cart.clear()
        return redirect("order_detail",order.id)


class AddressAPIView(APIView):
    def post(self, request, format=None):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderHistoryApi(APIView):
    def get(self, request):
        print(request.user.id)
        print("==========================================")
        queryset = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(queryset, many=True)
        return Response({'queryset': serializer.data})
    
# @api_view(['POST'])
# def cart_add(request,slug):
#     cart=CartAdd
#     product = Product.objects.filter(slug=slug)
#     serializer = CategorySerializer(category, many=True)
#     return Response({'category': serializer.data})


#==================================================================
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'
    
ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
CallbackURL = 'http://127.0.0.1:8080/order/verify/'

class OrderPay(View):
    def get(self,request,order_id):
        order=Order.objects.get(id=order_id)
        request.session['order_pay']={
            'order_id':order.id,
        }
        data = {
        "MerchantID": settings.MERCHANT,
        "Amount": order.total_price,
        "Description": description,
        "Phone": request.user.phone_number,
        "CallbackURL": CallbackURL,
    }
        data = json.dumps(data)
    # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        try:
            response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)
            if response.status_code == 200:
                response = response.json()
                if response['Status'] == 100:
                    return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']}
                else:
                    return {'status': False, 'code': str(response['Status'])}
            return response
        except requests.exceptions.Timeout:
            return {'status': False, 'code': 'timeout'}
        except requests.exceptions.ConnectionError:
            return {'status': False, 'code': 'connection error'}

class OrderVerify(View):
    def get(self,request,authority):
        order_id=request.session['order_pay']['order_id']
        order=Order.objects.get(id=int(order_id))
        data = {
        "MerchantID": settings.MERCHANT,
        "Amount": order.total_price,
        "Authority": authority,
    }
        data = json.dumps(data)
        # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        response = requests.post(ZP_API_VERIFY, data=data,headers=headers)
        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                order.is_paid=True
                order.save()
                return {'status': True, 'RefID': response['RefID']}
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response