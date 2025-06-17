from django import forms
from django.contrib.auth.models import User
class SignupForm(forms.ModelForm):#signupform definition
    class Meta:
        model=User#alreeady defined inside django.contrib.auth.models
        fields=['username','password','email','first_name','last_name']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()