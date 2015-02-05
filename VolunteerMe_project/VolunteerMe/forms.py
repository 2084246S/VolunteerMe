from django import forms
from VolunteerMe.models import Volunteer, Organiser, Search, Opportunities


class VolunteerForm(forms.ModelForm):
    firstname = forms.CharField(max_length=128, help_text='First name')
    surname = forms.CharField(max_length=128, help_text='Surname')
    email = forms.EmailField(help_text='Email')
    gender = forms.ChoiceField(initial = None, help_text = 'Gender')
    time_available = forms.ChoiceField(initial = None, help_text = 'times available')
    contact_number = forms.IntegerField(max_length=15, initial = None, help_text = 'Contact number')

    class Meta:
        model = Volunteer


class OrganiserForm(forms.ModelForm):
    company_name = forms.CharField(help_text = 'Organisation Name')
    company_email = forms.EmailField(help_text = 'Organisation Email')
    company_number = forms.IntegerField(help_text = 'Organisation Contact number')
    company_address = forms.CharField(help_text = 'Organisation address')

    class Meta:
        model = Organiser