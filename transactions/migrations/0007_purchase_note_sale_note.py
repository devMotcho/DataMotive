# Generated by Django 5.0.6 on 2024-07-17 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_purchase_created_purchase_updated_sale_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='note',
            field=models.TextField(blank=True, verbose_name='Note'),
        ),
        migrations.AddField(
            model_name='sale',
            name='note',
            field=models.TextField(blank=True, verbose_name='Note'),
        ),
    ]
