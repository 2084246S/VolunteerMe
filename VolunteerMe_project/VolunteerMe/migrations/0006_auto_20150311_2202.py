# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0005_auto_20150311_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='name',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
