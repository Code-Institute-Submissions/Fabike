# Generated by Django 3.1.4 on 2021-02-19 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20210125_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brakes',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
