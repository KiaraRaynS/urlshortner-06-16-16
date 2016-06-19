# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 12:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appurl', '0004_auto_20160618_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('view', models.IntegerField()),
                ('session', models.CharField(max_length=40)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]