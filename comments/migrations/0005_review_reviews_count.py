# Generated by Django 3.2.23 on 2024-04-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reviews_count',
            field=models.IntegerField(null=True),
        ),
    ]
