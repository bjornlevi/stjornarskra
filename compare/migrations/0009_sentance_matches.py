# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0008_auto_20160809_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentance',
            name='matches',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compare.Sentance'),
        ),
    ]
