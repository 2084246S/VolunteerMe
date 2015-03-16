# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0006_auto_20150311_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
