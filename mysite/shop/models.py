from django.db import models
from django.contrib.auth.models import User
from . import helper
from django.urls import reverse


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
    pic = models.ImageField(upload_to='upload/images', default='upload/images/no-img.jpg')
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


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField(max_length=2000)
    publish_date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    is_active_comment = models.BooleanField(default=False)
    DRAFT = 1
    PUBLISHED = 2
    REOPEN = 3
    Order_state = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (REOPEN, 'Reopen'),
    )
    status = models.IntegerField(
        choices=Order_state,
        default=DRAFT,
    )
    price = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    has_discount = models.BooleanField(default=False)
    super_price = models.DecimalField(max_digits=11, decimal_places=2, default=0, null=True, blank=True)
    DOWNLOAD = 1
    POSTAL = 2
    Product_types = (
        (DOWNLOAD, 'Download'),
        (POSTAL, 'Postal'),
    )
    type_of_product = models.IntegerField(
        choices=Product_types,
        default=DOWNLOAD
    )
    EXPRESS = 1
    NORMAL = 2
    TIEPAKS = 3
    Product_transportation_class = (
        (EXPRESS, 'Express Post'),
        (NORMAL, 'Normal Post'),
        (TIEPAKS, 'Tiepaks'),
    )
    transportation_class = models.IntegerField(
        choices=Product_transportation_class,
        null=True,
        blank=True
    )
    AVAILABLE = 1
    UNAVAILABLE = 2
    PREBUY = 3
    Product_In_Stock = (
        (AVAILABLE, 'Available'),
        (UNAVAILABLE, 'Unavailable'),
        (PREBUY, 'In Prebuy'),
    )
    available_in_stock = models.IntegerField(
        choices=Product_In_Stock,
        default=AVAILABLE
    )
    category = models.ManyToManyField(Category, blank=True)
    pic = models.ImageField(upload_to='upload/product/images', default='upload/images/no-img.jpg')
    summary = models.CharField(max_length=100, blank=True)
    image_gallery = models.ManyToManyField(Image_gallery, blank=True)
    files = models.ManyToManyField(File_gallery, blank=True)
    count_of_download = models.IntegerField(null=True)
    related_product = models.ManyToManyField('self', blank=True,
                                             verbose_name="Related Product")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])


class Order(models.Model):
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=11)
    address = models.TextField(max_length=500, blank=True)
    order_note = models.CharField(max_length=200, blank=True)
    ATPLACE = 1
    ONLINE = 2
    Payment_types = (
        (ATPLACE, 'At place'),
        (ONLINE, 'Online'),
    )
    payment_type = models.IntegerField(
        choices=Payment_types,
        default=ONLINE,

    )
    is_accept_agreement = models.BooleanField()
    COMPLETED = 1
    CANCELED = 2
    INPROGRESS = 3
    CHECKING = 4
    PAYMENTTING = 5
    Order_statuses = (
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
        (INPROGRESS, 'In progress'),
        (CHECKING, 'Checking'),
        (PAYMENTTING, 'Paymentting'),
    )
    order_status = models.IntegerField(
        choices=Order_statuses,
        default=CHECKING,
    )
    payment_tool = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    order_update_date = models.DateTimeField(blank=True, null=True)
    count_of_allow_download = models.IntegerField(default=10)
    date_of_expire_download = models.DateTimeField(blank=True, null=True)
    random_order_id = models.IntegerField(default=helper.random_int, unique=True)

    def __str__(self):
        return str(self.random_order_id)

    def get_total_cost(self):
        return sum(item.get_cost for item in self.items.all)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    def __str__(self):
        return 'Order id:%s Product:%s' % (self.order, self.product)

    def get_cost(self):
        return self.price * self.count


class Payment_log(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    payment_code = models.CharField(max_length=200, unique=True)
    bank_tracking_code = models.CharField(max_length=200, blank=True)
    INITIAL = 1
    TOBANK = 2
    FROMBANK = 3
    ERROR = 4
    COMPLETE = 5
    Payment_statuses = (
        (INITIAL, 'Initial'),
        (TOBANK, 'To Bank'),
        (FROMBANK, 'From Bank'),
        (ERROR, 'Error'),
        (COMPLETE, 'Complete'),
    )
    Payment_status = models.IntegerField(
        choices=Payment_statuses,
        default=INITIAL
    )
    message = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return 'Order Id:%s Payment Code:%s' % (self.order, self.payment_code)
