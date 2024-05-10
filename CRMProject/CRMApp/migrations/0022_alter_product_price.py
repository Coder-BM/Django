# Generated by Django 5.0.4 on 2024-05-07 09:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRMApp', '0021_alter_dealdetails_quantity_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
