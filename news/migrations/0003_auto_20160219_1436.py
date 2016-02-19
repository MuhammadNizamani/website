# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20160219_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Article'),
        ),
        migrations.AlterField(
            model_name='image',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Event'),
        ),
    ]
