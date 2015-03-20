# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerMe', '0005_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=128, choices=[(b'A', b'Administrative / Office Work'), (b'B', b'Advice / Information giving'), (b'C', b'Advocacy / Human Rights)'), (b'D', b'Arts ( music/drama/crafts)'), (b'E', b'Befriending / Mentoring'), (b'F', b'Campaigning / Lobbying'), (b'G', b'Care / Support worker'), (b'H', b'Catering'), (b'I', b'Charity Event Support'), (b'J', b'Charity Shops / Retail'), (b'K', b'Committee Work'), (b'L', b'Community / Economic Development Work'), (b'M', b'Computing'), (b'N', b'Conservation / Gardening'), (b'O', b'Counselling'), (b'P', b'Disaster / emergency relief'), (b'Q', b'Drivers'), (b'R', b'Driving / escorting'), (b'S', b'Equal Opportunities / Race relations'), (b'T', b'Event Management'), (b'U', b'Event Marshals'), (b'V', b'Finance / Accountancy'), (b'W', b'Fundraising'), (b'X', b'General Event Support'), (b'Y', b'Homebased Volunteering'), (b'Z', b'IT Support'), (b't', b'Justice / Legal assistance'), (b'a', b'Landscaping/course layout/maintenance'), (b'b', b'Languages / translating'), (b'c', b'Library / Information Management'), (b'd', b'Management / Business Skills'), (b'e', b'Marketing / PR / Media'), (b'f', b'Medical/Physiotherapy'), (b'g', b'On line Volunteering'), (b'h', b'Playschemes / Childrens Clubs'), (b'i', b'Practical /DIY'), (b'j', b'Research / Policy work'), (b'k', b'Residential volunteering'), (b'l', b'Security'), (b'm', b'Short term / seasonal working'), (b'n', b'Specialist / Technical'), (b'o', b'Sports / Outdoor activities'), (b'p', b'Technical Support'), (b'q', b'Tutoring / Supporting Learners'), (b'r', b'Volunteering for under 16s'), (b's', b'Youth Work')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.CharField(max_length=1, choices=[(b'v', b'volunteer'), (b'o', b'organiser')]),
            preserve_default=True,
        ),
    ]
