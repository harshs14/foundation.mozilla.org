# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-09 23:02
from __future__ import unicode_literals

from django.db import migrations, models

def create_default_categories(apps, schema_editor):
    BuyersGuideProductCategory = apps.get_model("buyersguide", "BuyersGuideProductCategory")
    categories = [
        "Toys & Games",
        "Smart Home",
        "Entertainment",
        "Wearables",
        "Health & Exercise",
        "Pets",
    ]

    for cat in categories:
        category, created = BuyersGuideProductCategory.objects.get_or_create(name=cat)


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0005_auto_20181002_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyersGuideProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={'verbose_name': 'Buyers Guide Product Category', 'verbose_name_plural': 'Buyers Guide Product Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ManyToManyField(blank=True, related_name='product', to='buyersguide.BuyersGuideProductCategory'),
        ),
        migrations.RunPython(create_default_categories, migrations.RunPython.noop),
    ]
