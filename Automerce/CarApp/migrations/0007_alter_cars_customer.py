# Generated by Django 4.2 on 2023-06-01 12:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CarApp', '0006_alter_cars_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='customer',
            field=models.ManyToManyField(related_name='cars', to=settings.AUTH_USER_MODEL),
        ),
    ]
