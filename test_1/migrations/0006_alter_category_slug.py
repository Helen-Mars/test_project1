# Generated by Django 3.2.15 on 2023-06-01 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_1', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
