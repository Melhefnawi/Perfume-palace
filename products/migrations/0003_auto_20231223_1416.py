# Generated by Django 3.2.23 on 2023-12-23 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20231221_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Men',
        ),
        migrations.RemoveField(
            model_name='category',
            name='Women',
        ),
    ]
