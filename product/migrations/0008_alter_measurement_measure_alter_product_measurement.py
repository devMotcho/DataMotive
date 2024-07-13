# Generated by Django 5.0.6 on 2024-07-12 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_measurement_alter_product_measurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='measure',
            field=models.CharField(default='Unit', max_length=100, unique=True, verbose_name='Measure'),
        ),
        migrations.AlterField(
            model_name='product',
            name='measurement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.measurement', verbose_name='Measurement'),
        ),
    ]
