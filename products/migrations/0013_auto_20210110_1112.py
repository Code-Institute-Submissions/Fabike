# Generated by Django 3.1.4 on 2021-01-10 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20210110_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='has_sizes',
            new_name='is_bike',
        ),
    ]