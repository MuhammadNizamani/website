# Generated by Django 2.0.10 on 2019-01-14 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0008_applicationperiod'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationperiod',
            name='name',
            field=models.CharField(default='Navn', max_length=50, verbose_name='Navn'),
            preserve_default=False,
        ),
    ]
