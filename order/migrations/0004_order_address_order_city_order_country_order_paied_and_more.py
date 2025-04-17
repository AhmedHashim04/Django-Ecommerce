# Generated by Django 5.1.1 on 2025-04-16 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='order',
            name='paied',
            field=models.BooleanField(default=False, verbose_name='Paied'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='order',
            name='postal_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Postal Code'),
        ),
    ]
