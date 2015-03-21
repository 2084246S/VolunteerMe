from django import forms
from VolunteerMe.models import UserProfile, Opportunity
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



class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = ('name','category','start_date','end_date','description','location','optional')
