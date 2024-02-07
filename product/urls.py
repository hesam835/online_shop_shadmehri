from django.urls import path
from .views import about_us,index,cycle,news,contact,get_details,subcategory,get_details_sub,get_product,product_list,product_detail

urlpatterns = [
    path('api/products/',get_details , name = "get_details"),
    path('api/subcategory/<slug:slug>/',get_details_sub , name = "subcategory"),
    path('about_us', about_us, name = 'about_us'),
    path('', index, name = 'index'),
    path('cycle', cycle, name = 'cycle'),
    path('news', news, name = 'news'),
    path('contact', contact, name = 'contact'),
    path('subcategory/<slug:slug>/', subcategory, name = 'subcategory'),
    path('list_product/<slug:slug>/', product_list , name = 'list_product'),
    path('api/list_product/<slug:slug>/', get_product, name = 'get_product'),
    path('product_detail',product_detail, name = 'product_detail'),

]