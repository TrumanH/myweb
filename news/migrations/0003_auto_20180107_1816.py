# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-07 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180107_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
