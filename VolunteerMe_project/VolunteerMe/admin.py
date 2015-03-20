from django.contrib import admin
from VolunteerMe.models import UserProfile, Volunteer, Opportunity
admin.site.register(Volunteer)
admin.site.register(UserProfile)
admin.site.register(Opportunity)