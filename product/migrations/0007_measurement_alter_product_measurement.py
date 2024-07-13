# Generated by Django 5.0.6 on 2024-07-12 22:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_category_category_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure', models.CharField(default='Unit.', max_length=100, unique=True, verbose_name='Measure')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='measurement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.measurement', verbose_name='Measurement'),
        ),
    ]
