# Generated by Django 2.1.5 on 2019-03-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20190315_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_update_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
