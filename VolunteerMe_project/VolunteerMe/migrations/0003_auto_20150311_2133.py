# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0002_auto_20150311_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='location',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='optional',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
