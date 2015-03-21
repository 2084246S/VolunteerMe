from django.contrib import admin
from VolunteerMe.models import UserProfile,  Opportunity, Application

admin.site.register(UserProfile)
admin.site.register(Opportunity)
admin.site.register(Application)