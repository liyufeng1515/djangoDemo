# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-05 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sxEdu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opus',
            name='imageTitle',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]