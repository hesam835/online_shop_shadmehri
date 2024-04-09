from django.urls import path
from .views import about_us,index,cycle,news,contact,get_details,subcategory,get_details_sub,get_product,product_list,product_detail,get_detail_product,get_discount,get_productfeature,get_news,get_users,comment,SearchAPIView,CommentAPIView

urlpatterns = [

    path('about_us', about_us, name = 'about_us'),
    path('comment/<slug:slug>/',comment, name = 'comment'),
    path('cycle', cycle, name = 'cycle'),
    path('', index, name = 'index'),
    path('news', news, name = 'news'),
    path('contact', contact, name = 'contact'),
    path('subcategory/<slug:slug>/', subcategory, name = 'subcategory'),
    path('list_product/<slug:slug>/', product_list , name = 'list_product'),
    path('product_detail/<slug:slug>/',product_detail, name = 'product_detail'),
    #========================api===========================
    path('api/list_product/<slug:slug>/', get_product, name = 'get_product'),
    path('api/product_detail/<slug:slug>/',get_detail_product, name = 'get_product_detail'),
    path('api/discount',get_discount,name="discount_api"),
    path('api/news/',get_news ,name="news_api"),
    path('api/productfeature/<slug:slug>/',get_productfeature,name ="productfeature_api"),
    path('api/users',get_users,name="get_user"),
    path('api/search',SearchAPIView.as_view(),name="search_api"),
    path('api/products/',get_details , name = "get_details"),
    path('api/subcategory/<slug:slug>/',get_details_sub , name = "subcategory"),
    path('api/comment/<slug:slug>/',CommentAPIView.as_view(),name="comment_api"),

]