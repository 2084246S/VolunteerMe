# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0003_auto_20150320_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(help_text=b'address', max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='contact_number',
            field=models.CharField(help_text=b'Contact number', max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(help_text=b'Email', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(help_text=b'Full Name', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='post_code',
            field=models.CharField(help_text=b'postcode', max_length=12, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='town',
            field=models.TextField(help_text=b'Town', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.CharField(max_length=1, choices=[(b'v', b'Volunteer'), (b'o', b'organiser')]),
            preserve_default=True,
        ),
    ]
