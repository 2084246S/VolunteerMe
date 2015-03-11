from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from VolunteerMe.models import Volunteer, Organiser, Search
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


def organiser(request):
    pass


def show_opportunity(request):
    pass


def dashboard(request):
    pass


def manage_opportunities(request):
    pass


def manage_opportunity(request):
    pass


def create_opportunity(request):
    pass


def manage_application(request):
    pass


def manage_applications(request):
    pass


def about(request):
    pass


def category(request):
    pass