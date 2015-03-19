# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0002_auto_20150319_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='job_name',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='contact_number',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='post_code',
            field=models.CharField(max_length=12, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='town',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
