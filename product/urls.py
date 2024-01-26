from django.urls import path
from .views import about_us,index,cycle,news,contact

urlpatterns = [
    path('add_item', about_us, name = 'add_item'),
    path('add_item', index, name = 'add_item'),
    path('add_item', cycle, name = 'add_item'),
    path('add_item', news, name = 'add_item'),
    path('add_item', contact, name = 'add_item'),

]