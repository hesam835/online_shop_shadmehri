from django.contrib import admin
from .models import Order,OrderItem,Cart,CartItem,Coupon


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Coupon)

# Register your models here.
