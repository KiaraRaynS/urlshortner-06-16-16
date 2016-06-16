# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appurl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='link',
            field=models.TextField(default='hold'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookmark',
            name='shortlink',
            field=models.CharField(default='hold', max_length=50),
            preserve_default=False,
        ),
    ]
