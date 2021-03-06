__author__ = '2063602T'

from django.conf.urls import patterns, url

from VolunteerMe import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^profile/$', views.profile, name='profile'),
                       # This is for some pretty jancky AJAX stuff
                       url(r'^profile_opps_applied_for/$', views.profile_opps_applied_for,
                           name='profile_opps_applied_for'),
                       # More dodgy AJAX
                       url(r'^send_reply/$', views.send_reply,
                           name='send_reply'),
                       url(r'^add_profile/', views.register_organiser, name='add_profile'),
                       url(r'^edit_profile/', views.edit_profile, name='edit_profile'),

                       url(r'^opportunity/(?P<opportunity_id>\d+)/$', views.show_opportunity, name='opportunity'),
                       # url(r'^dashboard/$',
                       # views.dashboard,
                       #     name='dashboard'),
                       url(r'^search/$', views.search, name='search'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^organiser/manage_opportunities/$', views.manage_opportunities,
                           name='manage_opportunities'),
                       url(r'^organiser/manage_opportunities/(?P<opportunity_id>[\w\-]+)/$', views.manage_opportunity,
                           name='manage_opportunity'),
                       url(r'^organiser/create_opportunities/$', views.create_opportunity, name='create_opportunity'),
                       url(r'^organiser/edit_opportunities/$', views.edit_opportunity, name='edit_opportunity'),
                       url(r'^volunteer/my_applications/$', views.manage_applications, name='applied_opportunities'),
                       url(r'^volunteer/my_applications/(?P<application_id>[\w\-]+/$)', views.manage_application,
                           name='my_application'),
                       url(r'^volunteer/application_replies/$', views.volunteer_replies, name="volunteer_replies"),
                       url(r'^organiser/reply_applications/$', views.manage_applications, name="reply_applications"),
                       url(r'^application/(?P<opportunity_id>\d+)/$', views.application_form, name="application_form"),
                       # link to a basic key word search view.
                       url(r'^suggest_job/$', views.suggest_job, name='suggest_job'),
                       url(r'^view_profile/(?P<profile_name>[\w\-]+)/$', views.view_profile, name='view_profile'),
                       url(r'^users/', views.users, name='users')
                       )

