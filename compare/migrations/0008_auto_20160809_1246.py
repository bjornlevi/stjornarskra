# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 12:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0007_auto_20160809_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='match',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
    ]
