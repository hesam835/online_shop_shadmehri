from django.urls import path
from .views import cart ,Cart_Add,CartRemoveApi,detail_cart,OrderCreate,OrderDetail,ShowCart

urlpatterns = [
    path('detail_cart' , detail_cart , name="detail_cart"),
    path('api/create_checkout/' , OrderCreate.as_view() , name="create_checkout"),    
    path('api/show_cart/' , ShowCart.as_view() , name="showcart"),    
    path('api/order_detail/<int:order_id>/' , OrderDetail.as_view() , name="order_detail"),    
    path('cart' , cart , name="cart"),
    path('api/cart_add/<slug:slug>/' , Cart_Add.as_view() , name="cart_add"),
    path('api/cart_remove/<slug:slug>/' , CartRemoveApi.as_view() , name="cart_remove")

]