# Generated by Django 5.1 on 2024-09-20 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDname', models.CharField(max_length=50)),
                ('PRDdescription', models.TextField(max_length=1000)),
            ],
        ),
    ]
