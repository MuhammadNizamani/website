# Generated by Django 3.1.2 on 2020-10-21 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_image_compressed'),
        ('inventory', '0010_item_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='files.image'),
        ),
    ]
