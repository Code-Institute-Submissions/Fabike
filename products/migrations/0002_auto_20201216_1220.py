# Generated by Django 3.1.4 on 2020-12-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url01',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image_url02',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]