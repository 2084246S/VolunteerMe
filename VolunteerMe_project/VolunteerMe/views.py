from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from VolunteerMe.models import Application, Opportunity, EditUserProfile,Reply
from VolunteerMe.forms import UserProfileForm, OpportunityForm, UserProfile, EditUserProfileForm,ApplicationForm
from VolunteerMe.google_address_search import run_query
from datetime import datetime
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required


# Homepage
# shows a list of newest and urgent placements
def index(request):
    # Make new context dictionary
    context_dict = dict()

    # Generate category list
    opp_list = Opportunity.objects.order_by('job_name')
    context_dict['categories'] = opp_list

    # generate "new Opportunities" list
    new_opportunities_list = Opportunity.objects.order_by('-start_date')[:5]
    context_dict['new_opportunities'] = new_opportunities_list

    # generate "ending soon" list
    ending_soon_list = Opportunity.objects.order_by('-end_date')[:5]
    context_dict['ending_soon'] = ending_soon_list

    return render(request, 'Volunteer_Me/index.html', context_dict)


# search page
def search(request):
    result_list = []

    return render(request, 'Volunteer_Me/search.html', {'result_list': result_list})


# volunteer opps applied for
def profile_opps_applied_for(request):
    u = User.objects.get(username=request.user.username)
    context_dict = {}
    try:
        up = UserProfile.objects.get(user=request.user)

    except:
        up = None

    applications = Application.objects.filter(volunteer=u)
    opportunities_list = []
    for application in applications:
        opportunities_list.append(application.opportunity)

    context_dict['opportunities_list'] = opportunities_list

    if up.type == 'o':
        organiser = Opportunity.company
        context_dict['opp'] = Opportunity.objects.filter(company=up)

    else:
        pass

    context_dict['user'] = u
    context_dict['userprofile'] = up

    return render(request, 'Volunteer_Me/profile_opps_applied_for.html', context_dict)


#user profile page
def profile(request):
    # get user information
    u = request.user

    context_dict = {}

    try:
        up = UserProfile.objects.get(user=request.user)

    except:
        up = None

    #if user is an organiser give back their jobs and
    # applications for their jobs
    if up.type == 'o':
        opportunities_list = Opportunity.objects.filter(company=up).order_by('-start_date')[:10]
        #context_dict['app'] = Application.objects.filter(company=up.name)
    #else give back jobs that are urgent and opportuinities applied for
    else:
        opportunities_list = Opportunity.objects.order_by('-start_date')[:10]
        #context_dict['app'] = Application.objects.filter(name=up.name)

    context_dict['opportunities_list'] = opportunities_list
    context_dict['user'] = u
    context_dict['userprofile'] = up

    return render(request, 'Volunteer_Me/profile.html', context_dict)


# place users into one of two groups
#<<<<<<< HEAD
def set_group(request, user, user_profile):
    if user_profile.type == 'o':
#=======
#def set_group(request, user):
#
#    if UserProfile.objects.filter(user=user).type == 'o':
#>>>>>>> 90b3f256309fd946fd4c234b7d70919e254330da
        g = Group.objects.get(name='organiser')
        g.user_set.add(user)
    else:
        g = Group.objects.get(name='volunteer')
        g.user_set.add(user)


# register
def register_organiser(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST)
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

                set_group(request, user, profile)

                return index(request)
    else:
        form = UserProfileForm(data=request.GET)
        return render(request, 'Volunteer_Me/organiser/organiser_register.html', {'profile_form': form})


#edit profile details
def edit_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            if request.user.is_authenticated():
                profile = profile_form.save(commit=False)
                user = User.objects.get(username=request.user.username)
                profile.user = user
                profile.type = user.type
                try:
                    profile.picture = request.FILES['picture']
                except:
                    pass
                profile.save()
                set_group(request, user)
                return index(request)
    else:
        form = UserProfileForm()
    return render(request, 'Volunteer_Me/organiser/organiser_register.html', {'profile_form': form})


#shows opportunity details
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
def volunteer_replies(request):

    u = User.objects.get(username=request.user.username)
    context_dict = {}
    try:
        up = UserProfile.objects.get(user=request.user)

    except:
        up = None
    applications = Application.objects.filter(volunteer=u)
    replies = Reply.objects.filter(answer=True,id=applications)
    opportunities_list = []
    for reply in replies:
        opportunities_list.append(reply.application)

    context_dict['opportunities_list'] = opportunities_list

    if up.type == 'o':
        organiser = Opportunity.company
        context_dict['opp'] = Opportunity.objects.filter(company=up)

    else:
        pass

    context_dict['user'] = u
    context_dict['userprofile'] = up

    return render(request,'Volunteer_Me/volunteer/volunteer_replies.html',context_dict)

@login_required
def manage_opportunities(request, opportunity_id):
    return render()

@login_required
#edit specific opportunites
def manage_opportunity(request, opportunity_id, username):
    opportunity = Opportunity.objects.get(id=opportunity_id).filter(username=username)
    if opportunity:
        edit_opportunity(request)

        opportunity.save()
    context = {'opportunity': opportunity}
    return render(request, 'Volunteer_Me/organiser/edit_opportunity.html', context)


@login_required
#create an opportunity
def create_opportunity(request):
    company = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        opp_form = OpportunityForm(request.POST)
        if opp_form.is_valid():
            if request.user.is_authenticated():
                profile = opp_form.save(commit=False)
                profile.company = company
                profile.save()
                return profile(request)
    else:
        form = OpportunityForm()
    return render(request, 'Volunteer_Me/organiser/new_opportunity.html', {'opportunity_form': form})


#edit current opportunities
def edit_opportunity(request):
    username = User.objects.get(username=request.user.username)
    company = UserProfile.objects.get(name=request.user)
    if request.method == 'POST':
        opp_form = OpportunityForm(request.POST)
        if opp_form.is_valid():
            if request.user.is_authenticated():
                profile = opp_form.save(commit=False)
                profile.company = company
                profile.save()
                return profile(request)
    else:
        form = OpportunityForm(request.GET)
    return render(request, 'Volunteer_Me/organiser/edit_opportunity.html', {'opportunity_form': form})

#organiser replies from volunteers
@login_required
def manage_applications(request):
    context_dict = {}
    u = User.objects.get(username=request.user.username)

    up = UserProfile.objects.filter(user = u)
    opportunites = Opportunity.objects.filter(company=up)
    app_list = []
    for opportunity in opportunites:
        applications = Application.objects.filter(opportunity =opportunity)
        for app in applications:
            app_list.append(app.volunteer)

    return render(request, 'Volunteer_Me/organiser/organiser_replies.html', context_dict)


#mange reply to volunteer
@login_required
def manage_application(request, application_id):
    application = Opportunity.objects.get(id=application_id)

    if application:
        application.save()

    context = {'application': application}
    return render(request, 'Volunteer_Me/volunteer/volunteer_replies.html', context)

#about page
def about(request):
    return render(request, 'Volunteer_Me/about.html')

#jobs list
def get_job_list(max_results=0, contains=''):
    job_list = []
    if contains:
        job_list = Opportunity.objects.filter(name__contains=contains)
    else:
        job_list = Opportunity.objects.all()
    if max_results > 0:
        if len(job_list) > max_results:
            job_list = job_list[:max_results]
    return job_list


# Retrieves the list of jobs that contain the string
# from the search box in their name
def suggest_job(request):
    contains = ''
    if request.method == 'GET':
        if 'suggestion' in request.GET:
            contains = request.GET['suggestion']  #get the sting to search for

    #get 8 placements which contain the string
    cat_list = get_job_list(8, contains)
    #render in list
#<<<<<<< HEAD
#    return render(request, 'Volunteer_Me/cats.html', {'cat_list': cat_list})
#=======
    return render(request, 'Volunteer_Me/cats.html', {'cat_list': cat_list})

def application_form(request, opportunity_id):
    if request.method == 'POST':
        application_form = ApplicationForm(request.POST)
        if application_form.is_valid():
            if request.user.is_authenticated():
                application = application_form.save(commit=False)
                application.opportunity = Opportunity.objects.get(id=opportunity_id)
                try:
                    profile.picture = request.FILES['picture']
                except:
                    pass
                profile.save()

                return index(request)
    else:
        form = ApplicationForm(request.GET)
    return render(request, 'Volunteer_Me/volunteer/applications_form.html', {'profile_form': form})
#>>>>>>> 90b3f256309fd946fd4c234b7d70919e254330da
