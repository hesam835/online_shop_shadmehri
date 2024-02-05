from django.contrib import admin
from .models import Order,OrderItem,Cart,CartItem,Coupon
class OrderlistPlay(admin.ModelAdmin):
    list_display=("total_price","is_paid")

class OrderItemListPlay(admin.ModelAdmin):
    list_display = ("quantity",)
    
class CouponnListPlay(admin.ModelAdmin):
    list_display = ("code","percent","deadline")
    
class TransAction(admin.ModelAdmin):
    list_display = ("final_price","teansactin_type")
    
    
admin.site.register(Order,OrderlistPlay)
admin.site.register(OrderItem,OrderItemListPlay)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Coupon,CouponnListPlay)

# Register your models here.