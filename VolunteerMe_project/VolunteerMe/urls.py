__author__ = '2063602T'

from django.conf.urls import patterns, url
from VolunteerMe import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^profile/$',
                           views.profile,
                           name='profile'),
                       url(r'^add_profile/', views.register_organiser, name='add_profile'),

                       url(r'^volunteer/register/$',
                           views.register_volunteer,
                           name='volunteer_registration'),

                       #url(r'^organiser/(?P<company_name>[\w\-]+)/$',
                       #    views.organiser,
                       #    name='organiser'),
                       url(r'^organiser/(?P<company>[\w\-]+)/(?P<opportunity_id>\d+)/$',
                           views.show_opportunity,
                           name='opportunity'),
                       url(r'^dashboard/$',
                           views.dashboard,
                           name='dashboard'),
                       url(r'^search/$',
                           views.search,
                           name='search'),
#                       I can't work out what this is for...
#                       I can't find a template that uses it.
#                       url(r'^category/(?P<category_name_slug>[\w\-]+)$',
#                           views.category,
#                           name='category'),
                       url(r'^about/$',
                           views.about,
                           name='about'),
                       url(r'^organiser/manage_opportunities/$',
                           views.manage_opportunities,
                           name='manage_opportunities'),
                       url(r'^organiser/manage_opportunities/(?P<opportunity_id>[\w\-]+)/$',
                           views.manage_opportunity,
                           name='manage_opportunity'),
                       url(r'^organiser/manage_opportunities/create/$',
                           views.create_opportunity,
                           name='create_opportunity'),
                       url(r'^volunteer/my_applications/$',
                           views.manage_applications,
                           name='my_applications'),
                       url(r'^volunteer/my_applications/(?P<application_id>[\w\-]+/$)',
                           views.manage_application,
                           name='my_application'),
                       url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
                       )

