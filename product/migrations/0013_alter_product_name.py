# Generated by Django 5.0.6 on 2024-08-17 21:34

import src.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=120, unique=True, validators=[src.validators.validate_names], verbose_name='Name'),
        ),
    ]
