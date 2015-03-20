from django.contrib import admin
from VolunteerMe.models import User, Volunteer,Organiser, Opportunity
admin.site.register(Volunteer)
admin.site.register(Organiser)
admin.site.register(Opportunity)