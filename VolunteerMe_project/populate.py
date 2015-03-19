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

    add_category(name = 'Administrative&Office Work')
    add_category(name = 'Advice & Information giving')
    add_category(name ='Advocacy & Human Rights')
    add_category(name = 'Arts ( music&drama&crafts)')
    add_category(name = 'Befriending & Mentoring')
    add_category(name = 'Campaigning & Lobbying')
    add_category(name ='Care & Support worker')
    add_category(name ='Catering')
    add_category(name = 'Charity Event Support')
    add_category(name ='Charity Shops & Retail')
    add_category(name ='Committee Work')
    add_category(name ='Community & Economic Development Work' )
    add_category(name ='Computing')
    add_category(name ='Conservation & Gardening')
    add_category(name = 'Counselling')
    add_category(name ='Disaster & emergency relief')
    add_category(name ='Drivers')
    add_category(name ='Driving & escorting')
    add_category(name = 'Equal Opportunities & Race relations')
    add_category(name ='Event Management')
    add_category(name ='Event Marshals')
    add_category(name ='Finance & Accountancy')
    add_category(name ='Fundraising')
    add_category(name = 'General Event Support')
    add_category(name ='Homebased Volunteering')
    add_category(name ='IT Support')
    add_category(name = 'Justice & Legal assistance')
    add_category(name ='Landscaping&course layout&maintenance')
    add_category(name = 'Languages & translating')
    add_category(name ='Library & Information Management')
    add_category(name ='Management & Business Skills')
    add_category(name = 'Marketing & PR & Media')
    add_category(name = 'Medical&Physiotherapy')
    add_category(name ='On line Volunteering')
    add_category(name ='Playschemes & Childrens Clubs')
    add_category(name =  'Practical &DIY')
    add_category(name ='Research & Policy work')
    add_category(name = 'Residential volunteering')
    add_category(name = 'Security')

    add_category(name = 'Short term & seasonal working')
    add_category(name ='Specialist & Technical')
    add_category(name = 'Sports & Outdoor activities')

    add_category(name ='Technical Support')

    add_category(name = 'Tutoring & Supporting Learners')
    add_category(name = 'Volunteering for under 16s')
    add_category(name = 'Youth Work')



    u_brian = add_user('brian123', 'brian123@test.com', 'pass123')
    o_brian = add_organiser('brian', u_brian)
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


def add_organiser(name, user):
    global company_number
    company_number += 1
    o = User.objects.get_or_create(user=user, username=name, company_number=company_number)[0]
    o.save()
    return o


def add_user(username, email, password):
    o = User.objects.get_or_create(username=username)[0]
    o.email = email
    o.password = password
    o.save()
    return o

def add_category(name):
    o = Category.objects.get_or_create(category=name)[0]
    o.save()
    return o

# Start execution here!
if __name__ == '__main__':
    print "Starting VolunteerMe population script..."
    populate()