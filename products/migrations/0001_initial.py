# Generated by Django 3.1.4 on 2020-12-16 12:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('BIKES', 'BIKES'), ('FRAMES', 'FRAMES')], default='BIKES', max_length=20)),
                ('product_group', models.CharField(choices=[('URBAN', 'URBAN'), ('ALL ROAD', 'ALL ROAD'), ('ROAD', 'ROAD')], default='URBAN', max_length=20)),
                ('name', models.CharField(max_length=80)),
                ('frame', models.CharField(max_length=80)),
                ('title', models.TextField(max_length=120)),
                ('fork', models.CharField(max_length=80)),
                ('wheels', models.CharField(blank=True, max_length=80, null=True)),
                ('tyres', models.CharField(blank=True, max_length=80, null=True)),
                ('max_tyre_size', models.CharField(blank=True, max_length=80, null=True)),
                ('crankset', models.CharField(blank=True, max_length=80, null=True)),
                ('shift_levers', models.CharField(blank=True, max_length=80, null=True)),
                ('derailleurs', models.CharField(blank=True, max_length=80, null=True)),
                ('casette_or_sprocket', models.CharField(blank=True, max_length=80, null=True)),
                ('chain_or_belt', models.CharField(blank=True, max_length=80, null=True)),
                ('brakes', models.CharField(blank=True, max_length=80, null=True)),
                ('handlebar', models.CharField(blank=True, max_length=80, null=True)),
                ('stem', models.CharField(blank=True, max_length=80, null=True)),
                ('saddle', models.CharField(blank=True, max_length=80, null=True)),
                ('seatpost', models.CharField(blank=True, max_length=80, null=True)),
                ('seat_clamp', models.CharField(blank=True, max_length=80, null=True)),
                ('headset', models.CharField(blank=True, max_length=80, null=True)),
                ('seatpost_diameter', models.CharField(blank=True, max_length=20, null=True)),
                ('bottom_bracket', models.CharField(blank=True, max_length=80, null=True)),
                ('dropouts', models.CharField(blank=True, max_length=120, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('weight_alloy', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('weight_carbon', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('price_alloy', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('price_carbon', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('price_comment', models.CharField(max_length=120)),
                ('product_image02', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
