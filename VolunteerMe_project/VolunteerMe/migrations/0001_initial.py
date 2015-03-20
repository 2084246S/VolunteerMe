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
                ('category', models.CharField(max_length=128, choices=[(b'A', b'Administrative / Office Work'), (b'B', b'Advice / Information giving'), (b'C', b'Advocacy / Human Rights)'), (b'D', b'Arts ( music/drama/crafts)'), (b'E', b'Befriending / Mentoring'), (b'F', b'Campaigning / Lobbying'), (b'G', b'Care / Support worker'), (b'H', b'Catering'), (b'I', b'Charity Event Support'), (b'J', b'Charity Shops / Retail'), (b'K', b'Committee Work'), (b'L', b'Community / Economic Development Work'), (b'M', b'Computing'), (b'N', b'Conservation / Gardening'), (b'O', b'Counselling'), (b'P', b'Disaster / emergency relief'), (b'Q', b'Drivers'), (b'R', b'Driving / escorting'), (b'S', b'Equal Opportunities / Race relations'), (b'T', b'Event Management'), (b'U', b'Event Marshals'), (b'V', b'Finance / Accountancy'), (b'W', b'Fundraising'), (b'X', b'General Event Support'), (b'Y', b'Homebased Volunteering'), (b'Z', b'IT Support'), (b't', b'Justice / Legal assistance'), (b'a', b'Landscaping/course layout/maintenance'), (b'b', b'Languages / translating'), (b'c', b'Library / Information Management'), (b'd', b'Management / Business Skills'), (b'e', b'Marketing / PR / Media'), (b'f', b'Medical/Physiotherapy'), (b'g', b'On line Volunteering'), (b'h', b'Playschemes / Childrens Clubs'), (b'i', b'Practical /DIY'), (b'j', b'Research / Policy work'), (b'k', b'Residential volunteering'), (b'l', b'Security'), (b'm', b'Short term / seasonal working'), (b'n', b'Specialist / Technical'), (b'o', b'Sports / Outdoor activities'), (b'p', b'Technical Support'), (b'q', b'Tutoring / Supporting Learners'), (b'r', b'Volunteering for under 16s'), (b's', b'Youth Work')])),
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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=1, choices=[(b'v', b'volunteer'), (b'o', b'organiser')])),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=75)),
                ('contact_number', models.CharField(max_length=15)),
                ('post_code', models.CharField(max_length=12, blank=True)),
                ('address', models.CharField(max_length=128, blank=True)),
                ('town', models.CharField(max_length=128, blank=True)),
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
            field=models.ForeignKey(to='VolunteerMe.Volunteer'),
            preserve_default=True,
        ),
    ]
