# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0008_auto_20150317_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opportunity', models.ForeignKey(to='VolunteerMe.Opportunity')),
                ('volunteer', models.ForeignKey(to='VolunteerMe.Volunteer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('application', models.ForeignKey(to='VolunteerMe.Application')),
            ],
            options={
                'verbose_name_plural': 'Replies',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='search',
            name='category',
        ),
    ]
