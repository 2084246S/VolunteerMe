# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunity',
            name='company_name',
        ),
        migrations.AddField(
            model_name='opportunity',
            name='company',
            field=models.ForeignKey(default=None, to='VolunteerMe.Organiser'),
            preserve_default=True,
        ),
    ]
