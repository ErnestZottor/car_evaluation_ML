# Generated by Django 3.2.6 on 2021-08-15 10:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20210815_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breastcancerchecker',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
