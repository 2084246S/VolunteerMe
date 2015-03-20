#!python.exe
import os
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VolunteerMe_project.settings')

import django

django.setup()

from VolunteerMe.models import Opportunity,User,Category
from django.contrib.auth.models import User



global company_number
company_number = 0


def populate():





    u_brian = add_user('brian123', 'brian123@test.com', 'pass123')
    o_brian = add_userprofile('brian123',type='organiser',name='Brian',email= 'brian123@test.com')
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
    o.start_date = start_date.today()
    o.end_date = end_date.today()
    o.save()
    return o


def add_userprofile(username,type,name,email):
    global company_number
    company_number += 1
    o = User.objects.get_or_create(user=username,type=type, name=name,email=email, contact_number=company_number)[0]
    o.save()
    return o


def add_user(username, email, password):
    o = User.objects.get_or_create(username=username)[0]
    o.email = email
    o.password = password
    o.save()
    return o

def add_cat(name):
    c = Category.objects.get_or_create(category=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting VolunteerMe population script..."
    populate()