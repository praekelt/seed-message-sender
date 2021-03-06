# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-02-20 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("message_sender", "0016_outbound_resend")]

    operations = [
        migrations.AlterField(
            model_name="channel",
            name="channel_type",
            field=models.CharField(
                choices=[
                    (b"junebug", b"Junebug"),
                    (b"vumi", b"Vumi"),
                    (b"http_api", b"HTTP API"),
                ],
                default=b"junebug",
                max_length=20,
            ),
        )
    ]
