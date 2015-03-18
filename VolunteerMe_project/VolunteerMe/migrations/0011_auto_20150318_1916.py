# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0010_search_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='category',
            field=models.ForeignKey(default=b'', to='VolunteerMe.Category'),
            preserve_default=True,
        ),
    ]
