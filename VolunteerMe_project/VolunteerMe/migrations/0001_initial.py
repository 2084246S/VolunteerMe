# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('location', models.TextField(default=b'', blank=True)),
                ('optional', models.TextField(default=b'', blank=True)),
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
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=1, choices=[(b'v', b'Volunteer'), (b'o', b'organiser')])),
                ('name', models.CharField(help_text=b'Full Name', max_length=128)),
                ('email', models.EmailField(help_text=b'Email', max_length=75)),
                ('contact_number', models.CharField(help_text=b'Contact number', max_length=15)),
                ('post_code', models.CharField(help_text=b'postcode', max_length=12, blank=True)),
                ('address', models.CharField(help_text=b'address', max_length=128, blank=True)),
                ('town', models.TextField(help_text=b'Town', blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=32, choices=[(1, b'Male'), (2, b'Female'), (3, b'Other')])),
                ('time_available', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='company',
            field=models.ForeignKey(default=None, to='VolunteerMe.User'),
            preserve_default=True,
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
