# Generated by Django 3.1.3 on 2021-09-04 10:48

import apps.account_account.managers
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=15, null=True)),
                ('phone', models.CharField(blank=True, error_messages={'unique': 'A user with that phone already exists.'}, max_length=60, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('phone_verification_code', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_profile_image/')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('registration_address', models.CharField(max_length=300, null=True)),
                ('registration_lat', models.CharField(max_length=100, null=True)),
                ('registration_long', models.CharField(max_length=100, null=True)),
                ('registration_phone_type', models.CharField(max_length=100, null=True)),
                ('registration_phone_model', models.CharField(max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', apps.account_account.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CashilokFill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effected_to_cashelok', models.BooleanField(default=False)),
                ('amount', models.FloatField(default=0)),
                ('state', models.IntegerField(choices=[(0, 'ORDER TUSHDI'), (1, "TO'LOVNI KUTYAPTI"), (2, "TO'L0V QABUL QILINDI"), (3, 'QOLDIRILDI')], default=0)),
                ('payment_method', models.CharField(choices=[('click', 'Click'), ('payme', 'Payme'), ('on_hand', 'On hand')], max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cashelok_fills', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cashilok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.FloatField(default=0)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cashelok', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
