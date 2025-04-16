# Generated by Django 5.1.1 on 2025-04-15 23:16

import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('settings', '0002_rename_brddesc_brand_desc_rename_brdname_brand_name_and_more'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_pictures/', verbose_name='Image')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('parent', models.ForeignKey(blank=True, limit_choices_to={'parent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Parent Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Price')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Cost')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Product Image')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Stock')),
                ('overall_rating', models.FloatField(default=0.0, verbose_name='Overall Rating')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.brand', verbose_name='Brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category', verbose_name='Category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('viewed_by', models.ManyToManyField(blank=True, related_name='viewed_products', to='account.profile', verbose_name='Viewed By')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000, verbose_name='Review')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3, verbose_name='Rating')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_review', to='product.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_review', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
