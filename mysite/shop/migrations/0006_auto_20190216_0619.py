# Generated by Django 2.1.5 on 2019-02-16 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190214_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(max_length=2000),
        ),
    ]
