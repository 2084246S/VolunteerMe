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
            name='EditUserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Full Name', max_length=128)),
                ('email', models.EmailField(help_text=b'Email', max_length=75)),
                ('contact_number', models.CharField(help_text=b'Contact number', max_length=15)),
                ('post_code', models.CharField(help_text=b'postcode', max_length=12, blank=True)),
                ('address', models.CharField(help_text=b'address', max_length=128, blank=True)),
                ('town', models.CharField(help_text=b'Town', max_length=128, blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('category', models.CharField(default=b'Other', max_length=128)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('location', models.TextField(default=b'', blank=True)),
                ('optional', models.TextField(default=b'None', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.BooleanField(default=None)),
                ('application', models.ForeignKey(to='VolunteerMe.Application')),
            ],
            options={
                'verbose_name_plural': 'Replies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=1, choices=[(b'v', b'volunteer'), (b'o', b'organiser')])),
                ('name', models.CharField(help_text=b'Full Name', max_length=128)),
                ('email', models.EmailField(help_text=b'Email', max_length=75)),
                ('contact_number', models.CharField(help_text=b'Contact number', max_length=15)),
                ('post_code', models.CharField(help_text=b'postcode', max_length=12, blank=True)),
                ('address', models.CharField(help_text=b'address', max_length=128, blank=True)),
                ('town', models.CharField(help_text=b'Town', max_length=128, blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='company',
            field=models.ForeignKey(default=None, to='VolunteerMe.UserProfile'),
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
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
