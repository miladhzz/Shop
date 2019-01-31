from django.contrib import admin
from shop.models import Category, Tag, Image_gallery

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Image_gallery)
