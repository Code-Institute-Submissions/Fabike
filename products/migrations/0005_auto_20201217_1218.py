# Generated by Django 3.1.4 on 2020-12-17 12:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201216_1311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['pk']},
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_comment',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_group',
            field=models.CharField(choices=[('FRAME', 'FRAME'), ('URBAN', 'URBAN'), ('ALL ROAD', 'ALL ROAD'), ('ROAD', 'ROAD')], default='FRAME', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('BIKES', 'BIKES'), ('FRAMES', 'FRAMES')], default='FRAME', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight_alloy',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight_carbon',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]
