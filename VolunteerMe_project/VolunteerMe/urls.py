__author__ = '2063602T'

from django.conf.urls import patterns, url
from VolunteerMe import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^profile/(?P<username>[\W\-]+)/$',
                           views.profile,
                           name='profile'),
                       url(r'^volunteer/register/$',
                           views.register_volunteer,
                           name='volunteer_registration'),
                       url(r'^organiser/register/$',
                           views.register_organiser,
                           name='organiser_registration'),
                       url(r'^organiser/(?P<username>[\W\-]+)/$',
                           views.organiser,
                           name='organiser'),
                       url(r'^organiser/(?P<username>[\W\-]+)/(?P<opportunity_id>)',
                           views.show_opportunity,
                           name='opportunity'),
                       url(r'^dashboard/$',
                           views.dashboard,
                           name='dashboard'),
                       url(r'^search/$',
                           views.search,
                           name='search'),
                       url(r'^about/$',
                           views.about,
                           name='about'),
                       url(r'^organiser/manage_opportunities/$',
                           views.manage_opportunities,
                           name='manage_opportunities'),
                       url(r'^organiser/manage_opportunities/(?P<opportunity_id>[\W\-]+)/$',
                           views.manage_opportunity,
                           name='manage_opportunity'),
                       url(r'^organiser/manage_opportunities/create/$',
                           views.create_opportunity,
                           name='create_opportunity'),
                       url(r'^volunteer/my_applications/$',
                           views.manage_applications,
                           name='my_applications'),
                       url(r'^volunteer/my_applications/(?P<application_id>[\W\-]+/$)',
                           views.manage_application,
                           name='my_application'),
)