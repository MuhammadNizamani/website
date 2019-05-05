# Generated by Django 2.0.10 on 2019-05-05 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20190505_1733'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-pub_date',), 'permissions': (('can_view_internal_article', 'Can see internal articles'),)},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('time_start',), 'permissions': (('can_see_attendees', 'Can see attending, waitlist, register meetup in a event'), ('can_view_internal_event', 'Can see internal events'))},
        ),
    ]
