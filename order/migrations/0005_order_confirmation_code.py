# Generated by Django 5.1.1 on 2025-04-17 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_address_order_city_order_country_order_paied_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
