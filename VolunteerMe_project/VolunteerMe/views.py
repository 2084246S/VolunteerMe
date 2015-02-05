from django.shortcuts import render
from VolunteerMe.models import Category, Opportunity
from datetime import datetime


# Create your views here.
def index(request):
    # Make new context dictionary
    context_dict = dict()

    # Generate category list
    category_list = Category.objects.order_by('+job_name')
    context_dict['categories'] = category_list

    # generate "new Opportunities" list
    new_opportunities_list = Opportunity.objects.order_by('-start_date')[:5]
    context_dict['new_opportunities'] = new_opportunities_list

    # generate "ending soon" list
    ending_soon_list = Opportunity.objects.order_by('+end_date').filter(
        end_date__range=(datetime().now(), )
    )[:5]
    context_dict['ending_soon'] = ending_soon_list

    return render(request, 'VolunteerMe/index.html', context_dict)