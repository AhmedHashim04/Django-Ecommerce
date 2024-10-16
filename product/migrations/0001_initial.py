# Generated by Django 5.1 on 2024-10-17 17:44

import django.db.models.deletion
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('settings', '0001_initial'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATname', models.CharField(max_length=50, verbose_name='Category Name')),
                ('CATdesc', models.TextField(max_length=1000, verbose_name='Category Description')),
                ('CATimage', models.ImageField(upload_to='category_pictures/', verbose_name='Category Image')),
                ('CATslug', models.SlugField(blank=True, null=True, unique=True)),
                ('CATparent', models.ForeignKey(blank=True, limit_choices_to={'CATparent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Category Parent')),
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
                ('PRDname', models.CharField(max_length=40, verbose_name='Name')),
                ('PRDdesc', models.TextField(max_length=1000, verbose_name='Description')),
                ('PRDprice', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Price')),
                ('PRDcost', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Cost')),
                ('PRDcreated', models.DateTimeField(auto_now=True)),
                ('PRDimage', models.ImageField(upload_to='products/', verbose_name='Product Image')),
                ('PRDslug', models.SlugField(blank=True, null=True, unique=True)),
                ('PRDstock', models.PositiveIntegerField(default=0, verbose_name='Stock')),
                ('overall_rating', models.FloatField(default=0.0)),
                ('PRDBrand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.brand', verbose_name='Product Brand')),
                ('PRDcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category', verbose_name='Product Category')),
                ('PRDtags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('PRDview', models.ManyToManyField(blank=True, related_name='users_see_it', to='accounts.profile', verbose_name='User see It')),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'ProductImages',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REVcontent', models.TextField(max_length=1000, verbose_name='Product Review')),
                ('REVrating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3)),
                ('REVcreated_at', models.DateTimeField(auto_now_add=True)),
                ('REVproduct', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_review', to='product.product')),
                ('REVuser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
