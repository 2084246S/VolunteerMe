#!python.exe
import os
from datetime import date


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VolunteerMe_project.settings')

import django

django.setup()

from VolunteerMe.models import Opportunity, UserProfile,Application

from django.contrib.auth.models import User

from django.contrib.auth.models import Group


global company_number
company_number = 0


def populate():



    newgroup = Group.objects.create(name='volunteer')
    newgroup.save()
    newgroup = Group.objects.create(name='organiser')
    newgroup.save()



    u_brian = add_user('Brian', 'brian123', 'brian123@test.com', 'pass123')
    o_brian = add_userprofile(u_brian, type='o', name='Brian', email='brian123@test.com')
    u_ally = add_user('Ally','ally123','ally123@test.com', 'pass456')
    v_ally = add_userprofile(u_ally,type= 'v',name="Ally",email='ally123@test.com')
    add_opportunity(organiser=o_brian, name="Admin", description="Typing stuff up",
                    location="23 Stewart Drive, Stornoway", start_date=date.today(), end_date=date.today())

    add_opportunity(organiser=o_brian, name="Cleaning", description="Blah, Blah, Blah, Blah Blah.........",
                    location="Just down the road", start_date=date.today(), end_date=date.today())
    add_opportunity(organiser=o_brian, name="Something Completely Different",
                    description="You are expected to clean the surface of mars with a toothbrush.", location="Mars", start_date=date.today(), end_date=date.today())
    add_opportunity(organiser=o_brian, name="Running Around Shouting at People", description="", location="The moon", start_date=date.today(), end_date=date.today())
    add_opportunity(organiser=o_brian, name="Performing Open Heart Surgery",
                    description="Please do not kill your patients.", location="Not really sure.", start_date=date.today(), end_date=date.today())
    add_opportunity(organiser=o_brian, name="Blah", description="Blah", location="4 Privet Drive", start_date=date.today(), end_date=date.today())
    add_opportunity(organiser=o_brian, name="Shining Spoons", description="--------------------",
                    location="The land of cutlery", start_date=date.today(), end_date=date.today())
    # Print out what we have added to the user.
    for o in Opportunity.objects.all():
        print "- {0}".format(str(o))

    add_application(u_ally,Opportunity.objects.get(name="Admin"))


def add_opportunity(organiser, name, description="", location="", start_date=date.today(), end_date=date.today()):
    o = Opportunity.objects.get_or_create(company=organiser, name=name, start_date=start_date, end_date=end_date)[0]
    o.description = description
    o.location = location
    o.start_date = start_date.today()
    o.end_date = end_date.today()
    o.save()
    return o


def add_userprofile(user, type, name, email):
    global company_number
    company_number += 1
    o = UserProfile.objects.get_or_create(user=user, type=type, name=name, email=email, contact_number=company_number)[0]
    o.save()
    return o


def add_user(first_name, username, email, password):
    o = User.objects.get_or_create(first_name=first_name, username=username, email=email, password=password)[0]
    o.email = email
    o.password = password
    o.save()
    return o

def add_application(volunteer,opportunity):
    a = Application.objects.get_or_create(volunteer = volunteer,opportunity=opportunity)[0]
    a.save()

    return a

if __name__ == '__main__':
    print "Starting VolunteerMe population script..."
    populate()