# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 12:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appurl', '0005_viewcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewcount',
            name='bookmark',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appurl.Bookmark'),
            preserve_default=False,
        ),
    ]
