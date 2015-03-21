from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from VolunteerMe.models import Application, Opportunity
from VolunteerMe.forms import  UserProfileForm,OpportunityForm, UserProfile
from VolunteerMe.google_address_search import run_query
from datetime import datetime
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def index(request):
    # Make new context dictionary
    context_dict = dict()

    # Generate category list
    opp_list = Opportunity.objects.order_by('job_name')
    context_dict['categories'] = opp_list

    # generate "new Opportunities" list
    new_opportunities_list = Opportunity.objects.order_by('-start_date')[:10]
    context_dict['new_opportunities'] = new_opportunities_list

    # generate "ending soon" list
    ending_soon_list = Opportunity.objects.order_by('-end_date')[:10]
    context_dict['ending_soon'] = ending_soon_list

    return render(request, 'Volunteer_Me/index.html', context_dict)


# Placeholder!!
def search(request):

    result_list = []



    return render(request, 'Volunteer_Me/search.html', {'result_list': result_list})


# stub views
def profile(request):
    u = User.objects.get(username=request.user.username)

    context_dict = {}
    is_volunteer = request.user.groups.filter(name='volunteer').exists()
    try:
        up = UserProfile.objects.get(user=request.user)
    except:
        up = None

    context_dict['user'] = u
    context_dict['userprofile'] = up
    return render(request,'Volunteer_Me/profile.html',context_dict)


def register_organiser(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            if request.user.is_authenticated():
                profile = profile_form.save(commit=False)
                user = User.objects.get(username=request.user.username)
                profile.user = user
                try:
                    profile.picture = request.FILES['picture']
                except:
                    pass
                profile.save()
                g = Group.objects.get(name='organiser')
                g.user_set.add(user)


                return index(request)
    else:
        form = UserProfileForm(request.GET)
    return render(request, 'Volunteer_Me/organiser/organiser_register.html', {'profile_form': form})


def show_opportunity(request, opportunity_id):
    context = dict()

    opportunity = Opportunity.objects.get(id=opportunity_id)

    if opportunity:

        organiser = opportunity.company.user
        context['company_name'] = organiser.first_name

        context['opportunity_name'] = opportunity.name
        context['start_date'] = opportunity.start_date
        context['end_date'] = opportunity.end_date
        context['description'] = opportunity.description
        context['optional'] = opportunity.optional
        context['location'] = opportunity.location

        #Querey address to get lat long
        location_query_result = run_query(opportunity.location)

        if len(location_query_result) > 0:
            context['latitude'] = location_query_result[0]['lat'];
            context['longitude'] = location_query_result[0]['lng'];
        else:
            context['latitude'] = 0.0;
            context['longitude'] = 0.0;

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            if request.user.is_authenticated():
                profile = profile_form.save(commit=False)
                user = User.objects.get(username=request.user.username)
                profile.user = user
                try:
                    profile.picture = request.FILES['picture']
                except:
                    pass
                profile.save()
                g = Group.objects.get(name='organiser')
                g.user_set.add(user)


                return index(request)
    else:
        form = UserProfileForm(request.GET)

    context['profile_form'] = form
    context['opportunity'] = opportunity

    return render(request, 'Volunteer_Me/opportunity.html', context)


@login_required
def dashboard(request):
    pass


@login_required
#volunteer
def manage_opportunities(request,opportunity_id):
    context_dict ={}

    opp = Opportunity.objects.get(id=opportunity_id)
    applications = Application.objects.filter(opp=opp)


@login_required
def manage_opportunity(request, opportunity_id, username):
    opportunity = Opportunity.objects.get(id=opportunity_id).filter(username = username)
    if opportunity:
        # do stuff

        opportunity.save()
    context = {'opportunity': opportunity}
    return render(request, 'Volunteer_Me/organiser/edit_opportunity.html', context)


@login_required
#@permission_required('VolunteerMe.add_opportunity')
def create_opportunity(request):
    username = User.objects.get(username=request.user.username)
    company = UserProfile.objects.get(name=request.user)
    if request.method == 'POST':
        opp_form = OpportunityForm(request.POST)
        if opp_form.is_valid():
            if request.user.is_authenticated():
                profile = opp_form.save(commit=False)
                profile.company=company
                profile.save()
                return index(request)
    else:
        form = OpportunityForm(request.GET)
    return render(request, 'Volunteer_Me/organiser/new_opportunity.html', {'opportunity_form': form})


@login_required
def manage_applications(request):
    pass


@login_required
def manage_application(request, application_id):
    application = Opportunity.objects.get(id=application_id)

    if application:
        # do stuff
        application.save()

    context = {'application': application}
    return render(request, 'Volunteer_Me/volunteer/volunteer_replies.html', context)


def about(request):
    return render(request, 'Volunteer_Me/about.html')

def get_job_list(max_results=0, contains=''):
    job_list = []
    if contains:
        job_list = Opportunity.objects.filter(oppertunity_name__contains=contains)
    else:
        job_list = Opportunity.objects.all()
    if max_results > 0:
        if len(job_list) > max_results:
            job_list = job_list[:max_results]
    return job_list



def suggest_category(request):
    cat_list = []
    contains = ''
    if request.method == 'GET':
        contains = request.GET['suggestion']

    cat_list = get_job_list(8, contains)

    return render(request, 'Volunteer_Me/cats.html', {'cat_list': cat_list})

