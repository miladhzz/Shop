# Generated by Django 2.1.5 on 2019-03-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20190315_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_of_expire_download',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
