# Generated by Django 5.0.6 on 2024-07-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_sale_final_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='final_price',
        ),
        migrations.AddField(
            model_name='purchase',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Value in Euros', max_digits=8, verbose_name='Final Price'),
        ),
    ]
