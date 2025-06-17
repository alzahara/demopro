from django.shortcuts import render,redirect

# Create your views here.
from django.views import View
from Users.forms import SignupForm

class IndexView(View):
    def get(self,request):
        return render(request,'home.html')

class RegisterView(View):
    def post(self,request):#after form submission
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            user=form_instance.save(commit=False)#password
            #user.set_password(raw_data)
            user.set_password(form_instance.cleaned_data['password'])
            user.save()
            return redirect('home')

    def get(self,request):
        form_instance=SignupForm()
        return render(request,'register.html',{'form':form_instance})

#login view
from Users.forms import LoginForm
from django.contrib.auth import authenticate,login
from .views import SigninView
class SigninView(View):
    def post(self,request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            user=authenticate(username=name,password=pwd)
            #authenticate() returns user object if all the user credentials are correct else none
            if user:
                #starting session using current user
                login(request,user)
                return redirect('home')
            else:
                print("Invalid user credentials")
                return redirect('login')
    def get(self, request):
        form_instance = LoginForm()
        return render(request, 'login.html', {'form': form_instance})

#logout view
def logout(request):
    return render(request,'logout.html')