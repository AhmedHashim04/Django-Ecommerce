# Generated by Django 5.1 on 2024-09-19 01:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATname', models.CharField(max_length=50, verbose_name='Category Name')),
                ('CATdesc', models.TextField(max_length=1000, verbose_name='Category Description')),
                ('CATimage', models.ImageField(upload_to=None, verbose_name='Category Image')),
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
                ('PRDBrand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.brand', verbose_name='Product Brand')),
                ('PRDcart', models.ManyToManyField(related_name='users_cart_it', to='accounts.profile', verbose_name='User cart It')),
                ('PRDcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category', verbose_name='Product Category')),
                ('PRDlove', models.ManyToManyField(related_name='users_love_it', to='accounts.profile', verbose_name='User Love It')),
                ('PRDvariant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.variant', verbose_name='Product Variant')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-PRDcreated'],
            },
        ),
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ALTalternatives', models.ManyToManyField(related_name='ALTproducts', to='product.product')),
                ('ALTproduct', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='name_product', to='product.product')),
            ],
            options={
                'verbose_name': 'Alternative',
                'verbose_name_plural': 'Alternatives',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PIMGimage', models.ImageField(upload_to='products/', verbose_name='Product Image')),
                ('PIMGproduct', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'ProductImages',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='PRDimage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.productimage', verbose_name='Product Image'),
        ),
    ]
