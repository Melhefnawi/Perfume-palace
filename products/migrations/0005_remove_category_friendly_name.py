# Generated by Django 3.2.23 on 2024-01-01 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category_friendly_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='friendly_name',
        ),
    ]