from django.urls import path
from .views import about_us,index,cycle,news,contact

urlpatterns = [
    path('about_us', about_us, name = 'about_us'),
    path('index', index, name = 'index'),
    path('cycle', cycle, name = 'cycle'),
    path('news', news, name = 'news'),
    path('contact', contact, name = 'contact'),

]