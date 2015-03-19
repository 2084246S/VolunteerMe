# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_name', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('category', models.CharField(default=b'Other', max_length=128)),
                ('company_name', models.CharField(default=b'TEMP', max_length=128)),
<<<<<<< HEAD
                ('slug', models.SlugField(unique=True)),
=======
>>>>>>> 14144ac461c38db1b74e529022f72e303dccb2f5
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('location', models.TextField(default=b'', blank=True)),
                ('optional', models.TextField(default=b'', blank=True)),
<<<<<<< HEAD
=======
                ('slug', models.SlugField(unique=True)),
>>>>>>> 14144ac461c38db1b74e529022f72e303dccb2f5
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organiser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=128)),
                ('company_email', models.EmailField(max_length=75)),
                ('company_number', models.IntegerField()),
                ('company_address', models.CharField(max_length=128)),
                ('company_post_code', models.CharField(max_length=12, blank=True)),
                ('company_town', models.TextField(blank=True)),
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
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('town_or_postcode', models.CharField(max_length=128, blank=True)),
                ('distance_from', models.IntegerField(blank=True)),
                ('optional', models.CharField(max_length=128)),
                ('category', models.ForeignKey(to='VolunteerMe.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=75)),
                ('gender', models.CharField(max_length=32, choices=[(1, b'Male'), (2, b'Female'), (3, b'Other')])),
                ('time_available', models.DateField()),
                ('contact_number', models.CharField(max_length=15, blank=True)),
                ('post_code', models.CharField(max_length=12, blank=True)),
                ('address', models.CharField(max_length=128, blank=True)),
                ('town', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='application',
            name='opportunity',
            field=models.ForeignKey(to='VolunteerMe.Opportunity'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='volunteer',
            field=models.ForeignKey(to='VolunteerMe.Volunteer'),
            preserve_default=True,
        ),
    ]
