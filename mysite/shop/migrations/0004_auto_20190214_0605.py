# Generated by Django 2.1.5 on 2019-02-14 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190209_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='company_name',
        ),
        migrations.AddField(
            model_name='shop_user',
            name='address',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='shop_user',
            name='company_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
