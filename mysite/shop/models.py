from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    parentCategory = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                       verbose_name="Parent Category")

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title


class Image_gallery(models.Model):
    title = models.CharField(max_length=100, unique=True)
    pic = models.ImageField(upload_to='media/upload/images', default='media/upload/images/no-img.jpg')
    alt = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Image Gallery'
        verbose_name_plural = 'Image Gallery'


class Province(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=100, unique=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Shop_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nik_name = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=11)
    tel = models.CharField(max_length=11)
    profile_pic = models.ImageField(upload_to='media/upload/profile/images', default='media/upload/images/no-img.jpg')
    about = models.TextField(max_length=300, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.OneToOneField(City, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Shop User'
        verbose_name_plural = 'Shop User'

    def __str__(self):
        return self.user.username
