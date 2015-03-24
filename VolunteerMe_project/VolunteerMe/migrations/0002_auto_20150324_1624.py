# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='description',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
