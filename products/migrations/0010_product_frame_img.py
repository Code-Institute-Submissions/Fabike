# Generated by Django 3.1.4 on 2020-12-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20201225_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='frame_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]