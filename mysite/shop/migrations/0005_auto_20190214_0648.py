# Generated by Django 2.1.5 on 2019-02-14 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190214_0605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='extra_description',
            new_name='order_note',
        ),
    ]
