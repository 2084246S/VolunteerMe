#!python.exe
import os
from datetime import date
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VolunteerMe_project.settings')

import django
django.setup()

from VolunteerMe.models import Opportunity, Organiser

categories_list = ['Administrative / Office Work', 'Advice / Information giving','Advocacy / Human Rights',
                   'Arts ( music/drama/crafts)','Befriending / Mentoring','Campaigning / Lobbying','Care / Support worker',
                   'Catering','Charity Event Support','Charity Shops / Retail','Committee Work',
                   'Community / Economic Development Work','Computing','Conservation / Gardening','Counselling',
                   'Disaster / emergency relief','Drivers','Driving / escorting','Equal Opportunities / Race relations',
                   'Event Management','Event Marshals','Finance / Accountancy','Fundraising','General Event Support',
                   'Homebased Volunteering','IT Support','Justice / Legal assistance','Landscaping/course layout/maintenance',
                   'Languages / translating','Library / Information Management','Management / Business Skills',
                   'Marketing / PR / Media','Medical/Physiotherapy','On line Volunteering','Playschemes / Childrens Clubs',
                   'Practical /DIY','Research / Policy work','Residential volunteering','Security',
                   'Short term / seasonal working','Specialist / Technical','Sports / Outdoor activities','Technical Support',
                   'Tutoring / Supporting Learners','Volunteering for under 16s','Youth Work']

def populate():

    add_opportunity(name="Admin", description="Typing stuff up", location="234 Somewhere Drive")
    add_opportunity(name="Cleaning", description="Blah, Blah, Blah, Blah Blah.........", location="Just down the road")
    add_opportunity(name="Something Completely Different", description="You are expected to clean the surface of mars with a toothbrush.", location="Mars")
    add_opportunity(name="Running Around Shouting at People", description="", location="The moon")
    add_opportunity(name="Performing Open Heart Surgery", description="Please do not kill your patients.", location="Not really sure.")
    add_opportunity(name="Blah", description="Blah", location="4 Privet Drive")
    add_opportunity(name="Shining Spoons", description="--------------------", location="The land of cutlery")
    # Print out what we have added to the user.
    for o in Opportunity.objects.all():
        print "- {0}".format(str(o))

def add_opportunity( organiser, name="", description="", location="", start_date=date.today(), end_date=date.today()):
    o = Opportunity.objects.get_or_create(organiser, name=name, description=description, location=location, start_date=start_date, end_date=end_date)[0]
    o.save()
    return o

def add_organiser(name):
   o = Organiser.objects.get_or_create(company_name=name)[0]
   o.save()
   return o

# Start execution here!
if __name__ == '__main__':
    print "Starting VolunteerMe population script..."
    populate()