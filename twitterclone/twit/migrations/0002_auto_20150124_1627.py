# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twit',
            name='author',
            field=models.TextField(default=datetime.datetime(2015, 1, 24, 16, 27, 42, 241737, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='twit',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
