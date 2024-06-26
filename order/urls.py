from django.urls import path
from .views import cart ,Cart_Add,CartRemoveApi,detail_cart,OrderCreate,OrderDetail,ShowCart,AddressAPIView,order_history,OrderHistoryApi,OrderPay,OrderVerify,ShowAddressApi

urlpatterns = [
    path('order_detail/<int:order_id>' , detail_cart , name="order_detail"),
    path('create_checkout/' , OrderCreate.as_view() , name="create_checkout"),
    path("pay/<int:order_id>" , OrderPay.as_view(),name="pay"),
    path('order_history' , order_history , name="order_history"),
    path('cart' , cart , name="cart"),
    path("verify/" , OrderVerify.as_view(),name="order_verify"),
    #===========api=============
    path('api/show_cart/' , ShowCart.as_view() , name="showcart"),    
    path('api/order/order_detail/<int:order_id>/' , OrderDetail.as_view() , name="order_detail_api"),    
    path('api/cart_add/<slug:slug>/' , Cart_Add.as_view() , name="cart_add"),
    path('api/cart_remove/<slug:slug>/' , CartRemoveApi.as_view() , name="cart_remove"),
    path('api/address/', AddressAPIView.as_view(), name='address_api_order'),
    path('api/order_history/', OrderHistoryApi.as_view(), name='order_history_api'),
    path('api/showaddress/order/order_detail/<int:order_id>', ShowAddressApi.as_view(), name='show_address_api'),

]