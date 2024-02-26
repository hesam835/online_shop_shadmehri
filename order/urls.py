from django.urls import path
from .views import cart ,Cart_Add,CartRemoveApi,detail_cart,OrderCreate,OrderDetail,ShowCart,AddressAPIView

urlpatterns = [
    path('order_detail/<int:order_id>' , detail_cart , name="order_detail"),
    path('create_checkout/' , OrderCreate.as_view() , name="create_checkout"),    
    path('api/show_cart/' , ShowCart.as_view() , name="showcart"),    
    path('api/order/order_detail/<int:order_id>/' , OrderDetail.as_view() , name="order_detail_api"),    
    path('cart' , cart , name="cart"),
    path('api/cart_add/<slug:slug>/' , Cart_Add.as_view() , name="cart_add"),
    path('api/cart_remove/<slug:slug>/' , CartRemoveApi.as_view() , name="cart_remove"),
    path('api/address/', AddressAPIView.as_view(), name='address_api'),

]