# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 08:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyPerson',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('polls.person',),
        ),
    ]