__author__ = '2063602t'

from django import template
from VolunteerMe.models import Category
from datetime import date

register = template.Library()

@register.inclusion_tag('Volunteer_Me/category-choices.html')
def get_category_choices():
    return {'cats': Category.objects.all()}


@register.inclusion_tag('Volunteer_Me/categories.html')
def get_category_list():
    return {'cats': Category.objects.all()}


@register.simple_tag(takes_context=False)
def today():
    return date.today().strftime('%d/%m/%y')

# from VolunteerMe.forms import applicationForm

# This will be an application form template tag.
# we can use this on each opportunity page
# plus this can be used to obtain volunteer data for storage over time
