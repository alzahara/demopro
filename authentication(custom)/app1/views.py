from django.shortcuts import render,redirect

# Create your views here.
#class based using view class
from django.views import View
from app1.forms import SignupForm

class IndexView(View):
    def get(self,request):
        return render(request,'home.html')
#register view
class SignupView(View):

    def post(self,request):#after form submission
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            # user=form_instance.save(commit=False)#password
            # #user.set_password(raw_data)
            # user.set_password(form_instance.cleaned_data['password'])
            # user.save()

            #using UserCreationForm
            form_instance.save()
            return redirect('home')

    def get(self,request):
        form_instance=SignupForm()
        return render(request,'signup.html',{'form':form_instance})
from app1.forms import LoginForm
from django.contrib.auth import authenticate,login
class SigninView(View):
    def post(self,request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            # print(name,pwd)

            # user=user.objects.get(username=name)
            # if((user.password==pwd):
            #     "valid"
            # else:
            #     "Invalid"
            user=authenticate(username=name,password=pwd)
            #authenticate() returns user object if all the user credentials are correct else none
            if user:
                #starting session using current user
                login(request,user)
                u=request.user
                print(u.username)
                print(u.email)
                print(u.first_name)
                return redirect('home')

            else:
                print("Invalid user credentials")
                return redirect('signin')
    def get(self, request):
        form_instance = LoginForm()
        return render(request, 'login.html', {'form': form_instance})

from django.contrib.auth import logout

class SignoutView(View):
    def get(self, request):
        logout(request)
        return redirect('signin')