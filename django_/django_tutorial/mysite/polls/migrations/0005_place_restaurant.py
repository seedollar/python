# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20160907_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='polls.Place')),
                ('serves_burgers', models.BooleanField(default=False)),
                ('serves_sushi', models.BooleanField(default=False)),
            ],
        ),
    ]