from django.conf.urls import patterns, include, url
from django.contrib import admin
from VolunteerMe import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'VolunteerMe_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^volunteer-me/', include('VolunteerMe.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
)
