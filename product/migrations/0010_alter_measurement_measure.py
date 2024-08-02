# Generated by Django 5.0.6 on 2024-08-02 10:05

import product.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measure',
            field=models.CharField(default='Unit', max_length=100, unique=True, validators=[product.validators.validate_unit_of_measure], verbose_name='Measure'),
        ),
    ]
