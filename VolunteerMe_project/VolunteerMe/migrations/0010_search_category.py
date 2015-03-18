# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0009_auto_20150318_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='category',
            field=models.ForeignKey(default='other', to='VolunteerMe.Category'),
            preserve_default=False,
        ),
    ]
