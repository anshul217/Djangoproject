# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='twit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=25)),
                ('body', models.TextField()),
                ('twit_date', models.DateTimeField(verbose_name=b'date twitted')),
                ('likes', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
