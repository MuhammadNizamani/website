# Generated by Django 2.0.13 on 2019-03-25 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='navn')),
                ('description', models.TextField(default='', max_length=512, verbose_name='beskrivelse')),
                ('internal', models.BooleanField(default=False, verbose_name='intern')),
                ('hidden', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='starttidspunkt')),
                ('end', models.DateTimeField(verbose_name='sluttidspunkt')),
                ('parent_queue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='reservations.Queue', verbose_name='foreldrekø')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
