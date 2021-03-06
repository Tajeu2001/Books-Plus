from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Profile,Book,Rating


    
class Registration(UserCreationForm):
    email = forms.EmailField()

class Meta:
    model = User
    fields = ['username','email','password1','password2']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'location', 'profile_picture', 'bio', 'contact','location']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'description','publisher','cover', 'year','pdf')    

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['overall_score','book','user']        