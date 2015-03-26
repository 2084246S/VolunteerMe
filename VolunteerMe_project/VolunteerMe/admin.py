from django.contrib import admin

from VolunteerMe.models import UserProfile, Opportunity, Application, Reply


admin.site.register(UserProfile)
admin.site.register(Opportunity)
admin.site.register(Application)
admin.site.register(Reply)