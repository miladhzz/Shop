# Generated by Django 2.1.5 on 2019-03-15 17:11

from django.db import migrations, models
import shop.helper


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20190315_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='random_order_id',
            field=models.IntegerField(default=shop.helper.random_int, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='count_of_allow_download',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(1, 'Completed'), (2, 'Canceled'), (3, 'In progress'), (4, 'Checking'), (5, 'Paymentting')], default=4),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_update_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_tool',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.IntegerField(choices=[(1, 'At place'), (2, 'Online')], default=2),
        ),
    ]
