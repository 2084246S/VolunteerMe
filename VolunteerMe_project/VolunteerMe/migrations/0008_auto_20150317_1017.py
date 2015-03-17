# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0007_auto_20150315_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='organiser',
            name='company_post_code',
            field=models.CharField(max_length=12, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organiser',
            name='company_town',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='address',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='post_code',
            field=models.CharField(max_length=12, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='town',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
