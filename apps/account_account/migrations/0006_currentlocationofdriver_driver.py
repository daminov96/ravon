# Generated by Django 3.1.3 on 2021-09-19 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_account', '0005_currentlocationofdriver'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentlocationofdriver',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
