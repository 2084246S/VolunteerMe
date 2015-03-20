from django.contrib import admin
from VolunteerMe.models import User, Volunteer, Opportunity
admin.site.register(Volunteer)
admin.site.register(User)
admin.site.register(Opportunity)