# Generated by Django 2.1.5 on 2019-03-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20190315_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_of_expire_download',
            field=models.DateField(blank=True, null=True),
        ),
    ]
