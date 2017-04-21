# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-19 11:57
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_sender', '0010_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(max_length=64, unique=True)),
                ('channel_type', models.CharField(choices=[(b'junebug', b'Junebug'), (b'vumi', b'Vumi')], default=b'junebug', max_length=20)),
                ('concurrency_limit', models.IntegerField(default=0)),
                ('message_delay', models.IntegerField(default=0)),
                ('message_timeout', models.IntegerField(default=0)),
                ('default', models.BooleanField(default=False)),
                ('configuration', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
