from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from VolunteerMe.models import Volunteer, Organiser, Search
from VolunteerMe.forms import VolunteerForm, OrganiserForm

from VolunteerMe.models import Category, Opportunity
from datetime import datetime
from django.contrib.auth.models import User


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
    #pass
    u = User.objects.get(username=request.user.username)
    context_dict = {}
    if u.is_volunteer:
        try:
            up = Volunteer.objects.get(user=u)
        except:
            up = None

        context_dict['user'] = u
        context_dict['userprofile'] = up

        return(request,'Volunteer_Me/volunteer_profile',context_dict)
    else:
        try:
            up = Organiser.objects.get(user=u)
        except:
            up = None

        context_dict['user'] = u
        context_dict['userprofile'] = up
        return(request,'Volunteer_Me/organiser_profile',context_dict)

def register_volunteer(request):
    #pass
    if request.method == 'POST':
        profile_form = VolunteerForm(request.POST)
        if profile_form.is_valid():
            if request.user.is_authenticated():
                profile = profile_form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                profile.user = user
                try:
                    profile.picture = request.FILES['picture']
                except:
                    pass
                profile.save()
                return index(request)
    else:
        form = Volunteer(request.GET)
    return render(request, 'rango/volunteer_register.html', {'profile_form': form})



def register_organiser(request):
    if request.method == 'POST':
        profile_form = OrganiserForm(request.POST)
        if profile_form.is_valid():
            if request.user.is_authenticated():
                profile = profile_form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                profile.user = user
                try:
                    profile.picture = request.FILES['picture']
                except:
                    pass
                profile.save()
                return index(request)
    else:
        form = Organiser(request.GET)
    return render(request, 'rango/organiser_register.html', {'profile_form': form})


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