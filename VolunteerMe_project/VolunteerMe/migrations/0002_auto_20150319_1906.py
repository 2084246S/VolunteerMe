# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('VolunteerMe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='company',
            field=models.ForeignKey(default=None, to='VolunteerMe.UserProfile'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
