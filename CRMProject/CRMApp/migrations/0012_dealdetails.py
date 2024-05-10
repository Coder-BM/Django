# Generated by Django 4.2.3 on 2023-07-20 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CRMApp', '0011_todaysschedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prod_name', models.CharField(max_length=100)),
                ('Quantity_Ordered', models.CharField(max_length=100)),
                ('Doc_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRMApp.doctor')),
                ('entered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
