# Generated by Django 5.1.1 on 2025-04-15 23:16

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Joined')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('address', models.TextField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Postal Code')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_pictures/', verbose_name='Profile Image')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
