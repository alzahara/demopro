from django import forms
from django.contrib.auth.models import User
# class SignupForm(forms.ModelForm):#signuoform definition

#     class Meta:
#         model=User#alreeady defined inside django.contrib.auth.models
#         fields=['username','password','email','first_name','last_name']
from app1.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
class SignupForm(UserCreationForm):

    role_choices=[('student','Student'),('teacher','Teacher'),('admin','Admin')]
    role=forms.ChoiceField(choices=role_choices,widget=forms.Select)
    class Meta:
        model=CustomUser
        fields=['username','password1','password2','email','first_name','last_name','phone','address','role']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)