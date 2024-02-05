from django.contrib import admin
from.models import Product,Category,Discount,ProductFeature,ProductFeatureValue,Comment,News
# Register your models here.

class ProductListPlay(admin.ModelAdmin):
    list_display = ("name","brand","price")

class CategoryListPlay(admin.ModelAdmin):
    list_display = ("name","is_sub")
    
class DiscountListPlay(admin.ModelAdmin):
    list_display = ("type","value","max_value")
    
class FeatureListPlay(admin.ModelAdmin):
    list_display = ("name",)
    
class FeatureValueListPlay(admin.ModelAdmin):
    list_display = ("value","product")
    
class CommentListPlay(admin.ModelAdmin):
    list_display = ("user_id","product_id")
    
class NewsListPlay(admin.ModelAdmin):
    list_display = ("title","create_by_user_id")
    
    
admin.site.register(Product,ProductListPlay)
admin.site.register(Category,CategoryListPlay)
admin.site.register(Discount,DiscountListPlay)
admin.site.register(ProductFeature,FeatureListPlay)
admin.site.register(ProductFeatureValue,FeatureValueListPlay)
admin.site.register(Comment,CommentListPlay)
admin.site.register(News,NewsListPlay)




