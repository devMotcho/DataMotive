# Generated by Django 5.0.6 on 2024-07-16 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_remove_sale_final_price_purchase_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='transaction_date',
            field=models.DateField(verbose_name='Transaction Date'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='transaction_date',
            field=models.DateField(verbose_name='Transaction Date'),
        ),
    ]
