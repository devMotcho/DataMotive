# Generated by Django 5.0.6 on 2024-08-04 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_measurement_measure'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]
