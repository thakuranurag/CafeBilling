# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-15 10:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_details_data',
            name='category',
        ),
        migrations.DeleteModel(
            name='category_data',
        ),
    ]
