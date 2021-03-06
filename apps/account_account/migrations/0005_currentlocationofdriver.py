# Generated by Django 3.1.3 on 2021-09-19 10:15

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_account', '0004_customuser_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentLocationOfDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('location_name', models.CharField(max_length=400)),
                ('latitude', models.CharField(max_length=150)),
                ('longtitude', models.CharField(max_length=150)),
                ('radius', models.FloatField(max_length=150)),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=32140)),
            ],
        ),
    ]
