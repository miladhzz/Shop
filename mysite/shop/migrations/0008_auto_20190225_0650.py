# Generated by Django 2.1.5 on 2019-02-25 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20190225_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_gallery',
            name='pic',
            field=models.ImageField(default='upload/images/no-img.jpg', upload_to='upload/images'),
        ),
    ]