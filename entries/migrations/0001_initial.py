# Generated by Django 3.0.2 on 2020-01-06 11:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.TextField()),
                ('date_time', models.DateTimeField(default=datetime.datetime.now)),
                ('journal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='entries.Journal')),
            ],
        ),
    ]
