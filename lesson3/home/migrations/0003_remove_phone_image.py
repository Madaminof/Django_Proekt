# Generated by Django 5.0 on 2024-05-01 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_phone_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='image',
        ),
    ]