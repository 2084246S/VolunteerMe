# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0004_remove_opportunity_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='name',
            field=models.CharField(default=b'Unnamed', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='opportunity',
            name='slug',
            field=models.SlugField(default=b'unnamed', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='category',
            field=models.CharField(default=b'Other', max_length=128),
        ),
    ]
