# Generated by Django 3.2.6 on 2021-08-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='breastcancerchecker',
            name='predictions',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
