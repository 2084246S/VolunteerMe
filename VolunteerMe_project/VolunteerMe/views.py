from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

from VolunteerMe.models import Application, Opportunity, Reply
from VolunteerMe.forms import UserProfileForm, OpportunityForm, UserProfile
from VolunteerMe.google_address_search import run_query



# Homepage
# shows a list of newest and urgent placements
def index(request):
    # Make new context dictionary
    context_dict = dict()

    # Generate category list
    opp_list = Opportunity.objects.order_by('category')
    context_dict['categories'] = opp_list

    # generate "new Opportunities" list
    new_opportunities_list = Opportunity.objects.order_by('-start_date')[:5]
    context_dict['new_opportunities'] = new_opportunities_list

    # generate "ending soon" list
    ending_soon_list = Opportunity.objects.order_by('end_date')[:5]
    context_dict['ending_soon'] = ending_soon_list

    return render(request, 'Volunteer_Me/index.html', context_dict)


# search page
def search(request):
    query = request.GET.get('suggestion', '')
    category = request.GET.get('category', '')

    result_list = Opportunity.objects.filter(name__contains=query) \
        .filter(category__contains=category) \
        .order_by('-end_date', 'name')

    print("Hello", result_list)
    return render(request, 'Volunteer_Me/search.html', {'result_list': result_list})


# volunteer opps applied for
@login_required
def profile_opps_applied_for(request):
    user = request.user
    context_dict = {}
    user_profile = UserProfile.objects.get(user=user)

    applications = Application.objects.filter(volunteer=user)
    opportunities_list = []
    for application in applications:
        opportunities_list.append(application.opportunity)

    context_dict['opportunities_list'] = opportunities_list

    if user_profile.type == 'o':
        context_dict['opp'] = Opportunity.objects.filter(company=user_profile)

    else:
        pass

    context_dict['user'] = user
    context_dict['userprofile'] = user_profile

    return render(request, 'Volunteer_Me/profile_opps_applied_for.html', context_dict)


# user profile page
@login_required
def profile(request):
    # get user information
    u = request.user

    context_dict = {}
    up = UserProfile.objects.get(user=request.user)

    # if user is an organiser give back their jobs and
    # applications for their jobs
    if up:
        if up.type == 'o':
            opportunities_list = Opportunity.objects.filter(company=up).order_by('-start_date')[:10]
            # context_dict['app'] = Application.objects.filter(company=up.name)
        # else give back jobs that are urgent and opportuinities applied for
        else:
            opportunities_list = Opportunity.objects.order_by('-start_date')[:10]
            # context_dict['app'] = Application.objects.filter(name=up.name)

    context_dict['opportunities_list'] = opportunities_list
    context_dict['user'] = u
    context_dict['userprofile'] = up

    return render(request, 'Volunteer_Me/profile.html', context_dict)


# place users into one of two groups
# not a view
def set_group(user, user_profile):
    if user_profile.type == 'o':
        g = Group.objects.get(name='organiser')
        g.user_set.add(user)
    else:
        g = Group.objects.get(name='volunteer')
        g.user_set.add(user)


# register
@login_required
def register_organiser(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST)
        if profile_form.is_valid():
            if request.user.is_authenticated():
                proposed_profile = profile_form.save(commit=False)
                user = request.user
                proposed_profile.user = user
                if request.FILES:
                    if 'picture' in request.FILES:
                        proposed_profile.picture = request.FILES['picture']
                proposed_profile.save()

                set_group(user, proposed_profile)

                return index(request)
    else:
        form = UserProfileForm(data=request.GET)
        return render(request, 'Volunteer_Me/organiser/organiser_register.html', {'profile_form': form})


# edit profile details
@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            if request.user.is_authenticated():
                user = request.user
                current_profile = UserProfile.objects.get(user=user)
                current_profile.type = user.type
                if request.FILES:
                    if 'picture' in request.FILES:
                        current_profile.picture = request.FILES['picture']

                current_profile.save()

                set_group(user, current_profile)
                return redirect('profile')
    else:
        form = UserProfileForm()
    return render(request, 'Volunteer_Me/organiser/organiser_register.html', {'profile_form': form})


# shows opportunity details
def show_opportunity(request, opportunity_id):
    context = dict()

    opportunity = Opportunity.objects.get(id=opportunity_id)

    if opportunity:

        organiser = opportunity.company.user
        context['company'] = organiser
        context['company_name'] = organiser.first_name

        context['opportunity_name'] = opportunity.name
        context['start_date'] = opportunity.start_date
        context['end_date'] = opportunity.end_date
        context['description'] = opportunity.description
        context['optional'] = opportunity.optional
        context['location'] = opportunity.location

        # Querey address to get lat long
        location_query_result = run_query(opportunity.location)

        if len(location_query_result) > 0:
            context['latitude'] = location_query_result[0]['lat']
            context['longitude'] = location_query_result[0]['lng']

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            if request.user.is_authenticated():
                proposed_profile = profile_form.save(commit=False)
                user = User.objects.get(username=request.user.username)
                proposed_profile.user = user
                try:
                    proposed_profile.picture = request.FILES['picture']
                except:
                    pass
                proposed_profile.save()
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
    # get user information
    u = request.user

    context_dict = {}

    try:
        up = UserProfile.objects.get(user=request.user)

    except:
        up = None

    opportunities_list = []
    applications = Application.objects.filter(volunteer=u)
    for application in applications:
        if len(Reply.objects.filter(application=application)) > 0:
            opportunities_list.append(
                {'opp': application.opportunity, 'reply': Reply.objects.filter(application=application)[0]})

    # opportunities_list =Opportunity.objects.order_by('-start_date')[:10]
    # context_dict['app'] = Application.objects.filter(name=up.name)

    context_dict['opportunities_list'] = opportunities_list
    context_dict['user'] = u
    context_dict['userprofile'] = up

    return render(request, 'Volunteer_Me/volunteer/volunteer_replies.html', context_dict)


@login_required
def manage_opportunities(request):
    u = request.user

    context_dict = {}
    up = UserProfile.objects.get(user=u)
    opportunity = Opportunity.objects.filter(company=up)

    context_dict['opportunites'] = opportunity
    context_dict['user'] = u
    context_dict['userprofile'] = up
    return render(request, 'Volunteer_Me/organiser/opportunities.html', context_dict)


@login_required
# edit specific opportunites

def manage_opportunity(request, opportunity_id):
    opportunity = Opportunity.objects.get(id=opportunity_id)
    company = UserProfile.objects.get(name=request.user)
    if request.method == 'POST':
        opp_form = OpportunityForm(request.POST)
        if opp_form.is_valid():
            if request.user.is_authenticated():
                new_opportunity = opp_form.save(commit=False)
                new_opportunity.company = company
                new_opportunity.save()
                return new_opportunity(request)
    else:
        form = OpportunityForm(request.GET)
    return render(request, 'Volunteer_Me/organiser/edit_opportunity.html', {'opportunity_form': form})


@login_required
# create an opportunity
def create_opportunity(request):
    company = request.user
    if request.method == 'POST':
        opp_form = OpportunityForm(data=request.POST)
        if opp_form.is_valid():
            if request.user.is_authenticated():
                new_opportunity = opp_form.save(commit=False)
                new_opportunity.company = UserProfile.objects.get(user=request.user)
                new_opportunity.save()

                return redirect('profile')

    form = OpportunityForm()
    return render(request, 'Volunteer_Me/organiser/new_opportunity.html', {'opportunity_form': form})


# edit current opportunities
@login_required
def edit_opportunity(request):
    company = UserProfile.objects.get(name=request.user)
    if request.method == 'POST':
        opp_form = OpportunityForm(request.POST)
        if opp_form.is_valid():
            if request.user.is_authenticated():
                new_opportunity = opp_form.save(commit=False)
                new_opportunity.company = company
                new_opportunity.save()
                return new_opportunity(request)
    else:
        form = OpportunityForm(request.GET)
    return render(request, 'Volunteer_Me/organiser/edit_opportunity.html', {'opportunity_form': form})


# organiser replies from volunteers
@login_required
def manage_applications(request):
    context_dict = {}
    u = request.user

    up = UserProfile.objects.filter(user=u)
    opportunities = Opportunity.objects.filter(company=up)
    app_list = []
    app_up = {}
    for opportunity in opportunities:
        applications = Application.objects.filter(opportunity=opportunity)
        for app in applications:
            app_dict = {'app': app, 'up': UserProfile.objects.filter(user=app.volunteer)[0]}
            if Reply.objects.filter(application=app):
                app_dict['reply'] = Reply.objects.filter(application=app)[0]
            app_list.append(app_dict)

    context_dict['opportunities'] = opportunities
    context_dict['applications'] = app_list
    return render(request, 'Volunteer_Me/organiser/organiser_replies.html', context_dict)


def send_reply(request):
    if request.method == 'POST':
        application_id = request.POST.get('app_id', '')

        application = Application.objects.get(id=application_id)
        if request.POST.get('undecided') and Reply.objects.get(application=application):
            Reply.objects.get(application=application).delete()
            return redirect('profile')

        reply = Reply.objects.get_or_create(application=application, answer=False)[0]
        if request.POST.get('accept'):
            reply.answer = True
        elif request.POST.get('decline'):
            reply.answer = False
        reply.save()

    return redirect('profile')


# manage reply to volunteer
@login_required
def manage_application(request, application_id):
    application = Opportunity.objects.get(id=application_id)

    if application:
        application.save()

    context = {'application': application}
    return render(request, 'Volunteer_Me/volunteer/volunteer_replies.html', context)


# about page
def about(request):
    return render(request, 'Volunteer_Me/about.html')


# jobs list
def get_job_list(max_results=0, contains=''):
    if contains != '':
        job_list = Opportunity.objects.filter(name__icontains=contains)
    else:
        job_list = Opportunity.objects.all()
    if max_results > 0:
        job_list = job_list[:max_results]
    return job_list


# Retrieves the list of jobs that contain the string
# from the search box in their name
def suggest_job(request):
    contains = ''
    category = ''
    if request.method == 'GET':
        if 'suggestion' in request.GET:
            contains = request.GET['suggestion']  # get the sting to search for
        if 'category' in request.GET:
            category = request.GET['category']

    # get 8 placements which contain the string
    job_list = get_job_list(8, contains, category)
    # render in list

    return render(request, 'Volunteer_Me/cats.html', {'job_list': job_list})


@login_required
def application_form(request, opportunity_id):
    # if request.user.is_authenticated():
    application = Application()
    application.volunteer = request.user
    application.opportunity = Opportunity.objects.get(id=opportunity_id)
    application.save()
    return redirect('profile')

def users(request):
    context_dict = {}
    profiles = UserProfile.objects.filter(type='o')
    context_dict['profiles'] = profiles
    return render(request, 'Volunteer_Me/users.html', context_dict)


def view_profile(request, profile_name):
    context_dict = {}
    user = User.objects.get(username=profile_name)
    context_dict['user'] = user
    profile = UserProfile.objects.get(user=user)
    context_dict['profile'] = profile
    opps = Opportunity.objects.filter(company = profile)
    context_dict['opportunites'] = opps
    return render(request, 'Volunteer_Me/view_profile.html', context_dict)
