# Generated by Django 3.1.4 on 2020-12-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_price_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_group',
            field=models.CharField(choices=[('CARBON', 'CARBON'), ('TITANIUM', 'TITANIUM'), ('URBAN', 'URBAN'), ('ALL ROAD', 'ALL ROAD'), ('ROAD', 'ROAD')], default='CARBON', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('BIKES', 'BIKES'), ('FRAMES', 'FRAMES')], default='FRAMES', max_length=20),
        ),
    ]
