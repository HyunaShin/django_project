# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-01 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StarRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_rate', models.TextField(max_length=1)),
            ],
        ),
    ]
