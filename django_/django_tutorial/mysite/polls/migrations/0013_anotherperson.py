# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_person_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnotherPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=100)),
                ('second', models.CharField(max_length=100)),
            ],
        ),
    ]