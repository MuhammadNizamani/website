# Generated by Django 2.0.10 on 2019-05-08 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20190508_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='event',
            name='date_start',
        ),
        migrations.RemoveField(
            model_name='event',
            name='hour_end',
        ),
        migrations.RemoveField(
            model_name='event',
            name='hour_start',
        ),
    ]
