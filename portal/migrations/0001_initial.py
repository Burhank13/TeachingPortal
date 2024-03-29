# Generated by Django 3.1.7 on 2021-08-31 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('link', models.URLField()),
                ('upload_time', models.DateTimeField(default=datetime.datetime.now)),
                ('deadline', models.DateTimeField()),
                ('marks_available', models.PositiveIntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('link', models.URLField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('marks_available', models.PositiveIntegerField(default=20)),
            ],
        ),
    ]
