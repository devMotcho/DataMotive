# Generated by Django 5.0.6 on 2024-07-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_measurement_measure_alter_product_measurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Value in Euros', max_digits=18, verbose_name='Price'),
        ),
    ]
