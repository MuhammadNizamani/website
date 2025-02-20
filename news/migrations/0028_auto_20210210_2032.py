# Generated by Django 3.1.1 on 2021-02-10 20:32

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0027_event_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='ingress_content',
            field=models.TextField(blank=True, help_text='En kort introduksjon til teksten', max_length=400, validators=[django.core.validators.MaxLengthValidator(400)], verbose_name='Ingress'),
        ),
        migrations.AlterField(
            model_name='article',
            name='internal',
            field=models.BooleanField(default=False, verbose_name='Intern artikkel'),
        ),
        migrations.AlterField(
            model_name='article',
            name='main_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Brødtekst'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Tittel'),
        ),
        migrations.AlterField(
            model_name='event',
            name='ingress_content',
            field=models.TextField(blank=True, help_text='En kort introduksjon til teksten', max_length=400, validators=[django.core.validators.MaxLengthValidator(400)], verbose_name='Ingress'),
        ),
        migrations.AlterField(
            model_name='event',
            name='main_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Hovedtekst'),
        ),
    ]
