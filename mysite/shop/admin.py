from django.contrib import admin
from shop import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Image_gallery)
admin.site.register(models.City)
admin.site.register(models.Province)
admin.site.register(models.Product)
admin.site.register(models.File_gallery)
admin.site.register(models.Order)
admin.site.register(models.Payment_log)
admin.site.register(models.OrderItem)
