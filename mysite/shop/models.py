from django.db import models
from django.contrib.auth.models import User

from shop.Enums import Order_state, Product_transportation_class, Product_types, Product_In_Stock


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


class File_gallery(models.Model):
    title = models.CharField(max_length=100, unique=True)
    file = models.FileField(upload_to='media/upload/files')
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'File Gallery'
        verbose_name_plural = 'File Gallery'


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
    city = models.OneToOneField(City, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Shop User'
        verbose_name_plural = 'Shop User'

    def __str__(self):
        return self.user.username


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField(max_length=1000)
    publish_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    is_active_comment = models.BooleanField(default=False)
    status = models.CharField(
        max_length=50,
        choices=[(tag, tag.value) for tag in Order_state]
    )
    price = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    has_discount = models.BooleanField(default=False)
    super_price = models.DecimalField(max_digits=11, decimal_places=2, default=0, null=True, blank=True)
    type_of_product = models.CharField(
        max_length=50,
        choices=[(tag, tag.value) for tag in Product_types]
    )
    transportation_class = models.CharField(
        max_length=50,
        choices=[(tag, tag.value) for tag in Product_transportation_class],
        null=True,
        blank=True
    )
    available_in_stock = models.CharField(
        max_length=50,
        choices=[(tag, tag.value) for tag in Product_In_Stock],
        null=True,
        blank=True
    )
    category = models.ManyToManyField(Category, blank=True)
    pic = models.ImageField(upload_to='media/upload/product/images', default='media/upload/images/no-img.jpg')
    summary = models.CharField(max_length=100, blank=True)
    image_gallery = models.ManyToManyField(Image_gallery, blank=True)
    files = models.ManyToManyField(File_gallery, blank=True)
    count_of_download = models.IntegerField(null=True)
    related_product = models.ManyToManyField('self', blank=True,
                                             verbose_name="Related Product")
