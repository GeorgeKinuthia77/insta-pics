# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-21 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0002_auto_20191021_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='profiles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gram.Profile'),
        ),
    ]
