from django.contrib import admin
from shop.models import Category, Tag, Image_gallery, Shop_user, City, Province, Product, File_gallery

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Image_gallery)
admin.site.register(Shop_user)
admin.site.register(City)
admin.site.register(Province)
admin.site.register(Product)
admin.site.register(File_gallery)
