# Generated by Django 5.0.6 on 2024-08-04 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_alter_stock_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['id']},
        ),
    ]
