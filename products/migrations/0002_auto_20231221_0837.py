# Generated by Django 3.2.23 on 2023-12-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='Men',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='Women',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
