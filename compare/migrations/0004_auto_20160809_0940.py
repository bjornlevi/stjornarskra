# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0003_auto_20160809_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='sentances',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]