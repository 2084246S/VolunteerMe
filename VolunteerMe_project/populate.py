#!python.exe
import os
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VolunteerMe_project.settings')

import django

django.setup()

from VolunteerMe.models import Opportunity, Organiser
from django.contrib.auth.models import User

categories_list = ['Administrative / Office Work', 'Advice / Information giving', 'Advocacy / Human Rights',
                   'Arts ( music/drama/crafts)', 'Befriending / Mentoring', 'Campaigning / Lobbying',
                   'Care / Support worker',
                   'Catering', 'Charity Event Support', 'Charity Shops / Retail', 'Committee Work',
                   'Community / Economic Development Work', 'Computing', 'Conservation / Gardening', 'Counselling',
                   'Disaster / emergency relief', 'Drivers', 'Driving / escorting',
                   'Equal Opportunities / Race relations',
                   'Event Management', 'Event Marshals', 'Finance / Accountancy', 'Fundraising',
                   'General Event Support',
                   'Homebased Volunteering', 'IT Support', 'Justice / Legal assistance',
                   'Landscaping/course layout/maintenance',
                   'Languages / translating', 'Library / Information Management', 'Management / Business Skills',
                   'Marketing / PR / Media', 'Medical/Physiotherapy', 'On line Volunteering',
                   'Playschemes / Childrens Clubs',
                   'Practical /DIY', 'Research / Policy work', 'Residential volunteering', 'Security',
                   'Short term / seasonal working', 'Specialist / Technical', 'Sports / Outdoor activities',
                   'Technical Support',
                   'Tutoring / Supporting Learners', 'Volunteering for under 16s', 'Youth Work']

global company_number
company_number = 0


def populate():
    u_brian = add_user('brian123', 'brian123@test.com', 'pass123')
    o_brian = add_organiser('brian',u_brian)
    add_opportunity(organiser=o_brian, name="Admin", description="Typing stuff up", location="234 Somewhere Drive")
    add_opportunity(organiser=o_brian, name="Cleaning", description="Blah, Blah, Blah, Blah Blah.........",
                    location="Just down the road")
    add_opportunity(organiser=o_brian, name="Something Completely Different",
                    description="You are expected to clean the surface of mars with a toothbrush.", location="Mars")
    add_opportunity(organiser=o_brian, name="Running Around Shouting at People", description="", location="The moon")
    add_opportunity(organiser=o_brian, name="Performing Open Heart Surgery",
                    description="Please do not kill your patients.", location="Not really sure.")
    add_opportunity(organiser=o_brian, name="Blah", description="Blah", location="4 Privet Drive")
    add_opportunity(organiser=o_brian, name="Shining Spoons", description="--------------------",
                    location="The land of cutlery")
    # Print out what we have added to the user.
    for o in Opportunity.objects.all():
        print "- {0}".format(str(o))


def add_opportunity(organiser, name, description="", location="", start_date=date.today(), end_date=date.today()):
    o = Opportunity.objects.get_or_create(company=organiser, name=name)[0]
    o.description = description
    o.location = location
    o.start_date = start_date
    o.end_date = end_date
    o.save()
    return o


def add_organiser(name, user):
    global company_number
    company_number += 1
    o = Organiser.objects.get_or_create(user=user, company_name=name, company_number=company_number)[0]
    o.save()
    return o


def add_user(username, email, password):
    o = User.objects.create_user(username,email,password)
    return o


# Start execution here!
if __name__ == '__main__':
    print "Starting VolunteerMe population script..."
    populate()