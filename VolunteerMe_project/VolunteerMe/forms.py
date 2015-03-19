from django import forms
from VolunteerMe.models import UserProfile,Volunteer, Search, Opportunity
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
<<<<<<< Updated upstream
#    choice = forms.RadioSelect(choices=Vol.SCENERY_CHOICES, widget=forms.RadioSelect))
=======


>>>>>>> Stashed changes
    class Meta:
        model = User
        fields = ('username', 'password')



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'name', 'email', 'post_code', 'town', 'contact_number','address','type')



class VolunteerForm(forms.ModelForm,):
    gender = forms.ChoiceField(initial=None, help_text='Gender')
    time_available = forms.ChoiceField(initial=None, help_text='times available')

    class Meta:
        model = Volunteer
        fields = ('gender','time_available')

