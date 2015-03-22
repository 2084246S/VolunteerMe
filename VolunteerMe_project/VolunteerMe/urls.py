__author__ = '2063602T'

from django.conf.urls import patterns, url
from VolunteerMe import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^profile/$',views.profile, name='profile'),
                       #This is for some pretty jancky AJAX stuff
                       url(r'^profile_opps_applied_for/$',views.profile_opps_applied_for, name='profile_opps_applied_for'),
                       url(r'^add_profile/', views.register_organiser, name='add_profile'),
                       url(r'^edit_profile/',views.edit_profile,name='edit_profile'),

                       url(r'^opportunity/(?P<opportunity_id>\d+)/$',views.show_opportunity,name='opportunity'),
                       # url(r'^dashboard/$',
                       #     views.dashboard,
                       #     name='dashboard'),
                       url(r'^search/$', views.search, name='search'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^organiser/manage_opportunities/$', views.manage_opportunities, name='manage_opportunities'),
                       url(r'^organiser/manage_opportunities/(?P<opportunity_id>[\w\-]+)/$', views.manage_opportunity,
                           name='manage_opportunity'),
                       url(r'^organiser/create_opportunities/$', views.create_opportunity, name='create_opportunity'),
                       url(r'^organiser/edit_opportunities/$',views.edit_opportunity,name='edit_opportunity'),
                       url(r'^volunteer/my_applications/$',  views.manage_applications,name='applied_opportunities'),
                       url(r'^volunteer/my_applications/(?P<application_id>[\w\-]+/$)',views.manage_application,
                           name='my_application'),
                       url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
                       )

