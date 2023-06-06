# Generated by Django 4.2 on 2023-06-01 12:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CarApp', '0003_delete_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='colour',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='customer',
            field=models.ManyToManyField(blank=True, related_name='cars', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cars',
            name='engineType',
            field=models.CharField(max_length=64, null=True),
        ),
    ]