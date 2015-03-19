from django import forms
from VolunteerMe.models import UserProfile,Volunteer, Search, Opportunity
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username', 'password')



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'name', 'contact_number', 'email','address','town', 'post_code','type')



class VolunteerForm(forms.ModelForm,):
    gender = forms.ChoiceField(initial=None, help_text='Gender')
    time_available = forms.ChoiceField(initial=None, help_text='times available')

    class Meta:
        model = Volunteer
        fields = ('gender','time_available')

