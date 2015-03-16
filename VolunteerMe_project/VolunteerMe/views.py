from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from VolunteerMe.models import Volunteer, Organiser, Search, Opportunity
from VolunteerMe.forms import VolunteerForm, OrganiserForm

from VolunteerMe.models import Category, Opportunity
from datetime import datetime


# Create your views here.
def index(request):
    # Make new context dictionary
    context_dict = dict()

    # Generate category list
    category_list = Category.objects.order_by('job_name')
    context_dict['categories'] = category_list

    # generate "new Opportunities" list
    new_opportunities_list = Opportunity.objects.order_by('-start_date')[:5]
    context_dict['new_opportunities'] = new_opportunities_list

    # generate "ending soon" list
    ending_soon_list = Opportunity.objects.order_by('end_date').filter()[:5]
    context_dict['ending_soon'] = ending_soon_list

    return render(request, 'Volunteer_Me/index.html', context_dict)


# Placeholder!!
def search(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:

            result_list = run_query(query)

    return render(request, 'Volunteer_Me/search.html', {'result_list': result_list})


# stub views
def profile(request):
    pass


def register_volunteer(request):
    pass


def register_organiser(request):
    pass


def organiser(request, company_name):
    context = dict()

    organiser = Organiser.objects.get(company_name=company_name)
    context['organiser'] = organiser

    if organiser:
        # do stuff
        organiser.save()

    return render(request, 'volunteer_me/organiser/organiser_profile.html', context)


def show_opportunity(request, username, opportunity_id):
    context = dict()

    organiser = Organiser.objects.get(username=username)
    opportunity = None

    if organiser:
        context['company_name'] = organiser.company_name
        opportunity = Opportunity.objects.get(id=opportunity_id)

        if opportunity:
            context['opportunity_name'] = opportunity.name
            context['start_date'] = opportunity.start_date.__unicode__()
            context['end_date'] = opportunity.end_date.__unicode__()
            context['description'] = opportunity.description
            context['optional'] = opportunity.optional
            context['location'] = opportunity.location

    context['opportunity'] = opportunity
    return render(request, 'Volunteer_Me/opportunity.html')

def dashboard(request):
    pass


def manage_opportunities(request):
    pass


def manage_opportunity(request, opportunity_id):
    opportunity = Opportunity.objects.get(id=opportunity_id)
    if opportunity:
        # do stuff

        opportunity.save()
    context = {'opportunity': opportunity}
    return render(request, 'volunteer_me/organiser/edit_opportunity.html', context)


def create_opportunity(request):
    pass


def manage_applications(request):
    pass


def manage_application(request, application_id):
    application = Opportunity.objects.get(id=application_id)

    if application:
        # do stuff
        application.save()

    context = {'application': application}
    return render(request, 'volunteer_me/volunteer/volunteer_replies.html', context)


def about(request):
    return render(request, 'volunteerme/about.html')


'''
Again, not sure what this is for...
def category(request, category_name_slug):
    context_dict = dict()  # Initialise context dictionary

    category = Category.objects.get(category_name_slug=category_name_slug)

    if category:
        opportunities = Opportunity.objects.filter(category=category)

        if opportunities:
            context_dict[]
'''