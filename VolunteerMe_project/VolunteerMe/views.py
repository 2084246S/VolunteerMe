from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from VolunteerMe.models import Volunteer, Search, Opportunity
from VolunteerMe.forms import VolunteerForm, UserProfileForm
from VolunteerMe.models import Category, Opportunity
from datetime import datetime
from django.contrib.auth.models import User,Group


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
        oppertunities = Opportunity.objects.filter()
        #if query:
        #result_list = run_query(query)

    return render(request, 'Volunteer_Me/search.html', {'result_list': result_list})


# stub views
def profile(request):
    #pass
    u = User.objects.get(username=request.user.username)

    context_dict = {}
    # if u in Group.user_in_group:
    #     try:
    #         up = Volunteer.objects.get(user=u)
    #     except:
    #         up = None
    #
    #     context_dict['user'] = u
    #     context_dict['userprofile'] = up
    #
    #     return(request,'Volunteer_Me/volunteer/volunteer_profile',context_dict)
    # else:
    try:
        up = User.objects.get(user=u)
    except:
        up = None

    context_dict['user'] = u
    context_dict['userprofile'] = up
    return(request,'Volunteer_Me/organiser/organiser_profile',context_dict)

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
                g =Group.objects.get(name='volunteer')
                g.user_set.add(user)

                return index(request)
    else:
        form = VolunteerForm(request.GET)
    return render(request, 'Volunteer_Me/volunteer/volunteer_register.html', {'profile_form': form})



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



def show_opportunity(request, company, opportunity_id):
    #context = dict()

    #organiser = Organiser.objects.get(company_name)
    #opportunity = None

    #if organiser:
    #    context['company_name'] = organiser.company_name
    #    opportunity = Opportunity.objects.get(id=opportunity_id)

    #    if opportunity:
    #        context['opportunity_name'] = opportunity.name
    #        context['start_date'] = opportunity.start_date.__unicode__()
    #        context['end_date'] = opportunity.end_date.__unicode__()
    #        context['description'] = opportunity.description
    #        context['optional'] = opportunity.optional
    #        context['location'] = opportunity.location

    #context['opportunity'] = opportunity
    return render(request, 'Volunteer_Me/opportunity.html', {})


def dashboard(request):
    pass


def manage_opportunities(request):
    pass


def manage_opportunity(request, opportunity_id,username):
    opportunity = Opportunity.objects.get(id=opportunity_id).filter(username = username)
    if opportunity:
        # do stuff

        opportunity.save()
    context = {'opportunity': opportunity}
    return render(request, 'Volunteer_Me/organiser/edit_opportunity.html', context)


def create_opportunity(request):
    if request.method == 'POST':
        opp = Opportunity


def manage_applications(request):
    pass


def manage_application(request, application_id):
    application = Opportunity.objects.get(id=application_id)

    if application:
        # do stuff
        application.save()

    context = {'application': application}
    return render(request, 'Volunteer_Me/volunteer/volunteer_replies.html', context)


def about(request):
    return render(request, 'Volunteer_Me/about.html')

def get_category_list(max_results=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__istartswith=starts_with)

    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]

    return cat_list

def suggest_category(request):

    cat_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']

    cat_list = get_category_list(8, starts_with)

    return render(request, 'Volunteer_Me/cats.html', {'cat_list': cat_list })



def is_volunteer(user):
    return user.groups.filter(name='volunteer').exists()
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
