# Generated by Django 2.1.5 on 2019-03-13 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20190312_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_selection',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.Cart'),
        ),
    ]
