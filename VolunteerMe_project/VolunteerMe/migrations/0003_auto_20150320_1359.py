# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0002_auto_20150320_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='optional',
            field=models.TextField(default=b'None', blank=True),
            preserve_default=True,
        ),
    ]
