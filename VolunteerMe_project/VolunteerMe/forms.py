from django import forms
from VolunteerMe.models import Volunteer, Organiser, Search, Opportunity
from django.contrib.auth.models import User


class VolunteerForm(forms.ModelForm):
    firstname = forms.CharField(max_length=128, help_text='First name')
    surname = forms.CharField(max_length=128, help_text='Surname')
    email = forms.EmailField(help_text='Email')
    gender = forms.ChoiceField(initial=None, help_text='Gender')
    time_available = forms.ChoiceField(initial=None, help_text='times available')
    contact_number = forms.CharField(max_length=15, initial=None, help_text='Contact number')
    post_code = forms.CharField(max_length=12,blank=True)
    address = forms.CharField(max_length=128,blank=True)
    town = forms.TextField(blank=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Volunteer
        fields = ('username', 'email', 'password')


class OrganiserForm(forms.ModelForm):
    company_name = forms.CharField(max_length=128,help_text='Organisation Name')
    company_email = forms.EmailField(max_length=128,help_text='Organisation Email')
    company_number = forms.CharField(help_text='Organisation Contact number')
    company_address = forms.CharField(help_text='Organisation address')
    post_code = forms.CharField(max_length=12,blank=True)
    address = forms.CharField(max_length=128,blank=True)
    town = forms.TextField(blank=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Organiser
        fields = ('username', 'email', 'password')