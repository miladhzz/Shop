from django.db import models


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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Image Gallery'
        verbose_name_plural = 'Image Gallery'
