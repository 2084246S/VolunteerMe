from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from VolunteerMe.models import Volunteer,Application, Search, Opportunity, Category
from VolunteerMe.forms import VolunteerForm, UserProfileForm,OpportunityForm, UserProfile
from datetime import datetime
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required, permission_required


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
    ending_soon_list = Opportunity.objects.order_by('end_date')[:5]
    context_dict['ending_soon'] = ending_soon_list

    return render(request, 'Volunteer_Me/index.html', context_dict)


# Placeholder!!
def search(request):

    result_list = []



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
    username = User.objects.get(username=request.user)
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
    return render(request, 'Volunteer_Me/organiser/opportunities.html', {'profile_form': form})


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


from django import template
from django.contrib.auth.models import Group
register = template.Library()
@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False