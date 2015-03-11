# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0003_auto_20150311_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunity',
            name='time',
        ),
    ]
