# Generated by Django 3.1.6 on 2021-04-24 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0012_applicationgroup_project_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationGroupChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.PositiveIntegerField()),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.application')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.applicationgroup')),
            ],
        ),
        migrations.AlterField(
            model_name='application',
            name='group_choice',
            field=models.ManyToManyField(through='applications.ApplicationGroupChoice', to='applications.ApplicationGroup'),
        ),
    ]
