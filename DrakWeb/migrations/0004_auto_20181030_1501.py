# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-30 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DrakWeb', '0003_auto_20181025_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ID',
        ),
        migrations.AddField(
            model_name='user',
            name='ticket',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Username',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
