# Generated by Django 3.1.1 on 2021-04-12 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0012_auto_20210210_1725'),
        ('website', '0016_auto_20210412_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='thumb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='files.image', verbose_name='Bilde'),
        ),
    ]
