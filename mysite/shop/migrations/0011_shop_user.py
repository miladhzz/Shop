# Generated by Django 2.1.5 on 2019-02-02 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0010_auto_20190201_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik_name', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(max_length=11)),
                ('tel', models.CharField(max_length=11)),
                ('profile_pic', models.ImageField(default='media/upload/images/no-img.jpg', upload_to='media/upload/profile/images')),
                ('about', models.TextField(blank=True, max_length=300, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]