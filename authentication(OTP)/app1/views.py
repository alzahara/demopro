from django.shortcuts import render,redirect,HttpResponse


# Create your views here.
#class based using view class
from django.views import View
from app1.forms import SignupForm
from django.contrib import messages

class IndexView(View):
    def get(self,request):
        return render(request,'home.html')

class StudentHomeView(View):
    def get(self, request):
        return render(request, 'studenthome.html')

class TeacherHomeView(View):
    def get(self, request):
        return render(request, 'teacherhome.html')
class AdminHomeView(View):
    def get(self, request):
        return render(request, 'adminhome.html')

#register view
from django.core.mail import send_mail
class SignupView(View):

    def post(self,request):#after form submission
        print(request.POST)
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            print('hello')
            user=form_instance.save(commit=False)
            #user.set_password(raw_data)
            user.is_active=False#After otp verification it will set to True
            user.save()
            user.generate_otp()
            send_mail(
                "Django Auth OTP",
                 user.otp,
                "alzaharabasheer@gmail.com",
                [user.email],
                fail_silently=False,
            )
            return redirect('verify_otp')
        # else:
        #     return HttpResponse('hi')

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
            user=authenticate(username=name,password=pwd)
            #authenticate() returns user object if all the user credentials are correct else none
            if user and user.is_superuser == True:
                login(request, user)
                return redirect('admin')
            elif user and user.role=='student':
                login(request, user)
                return redirect('student')
            elif user and user.role=='teacher':
                login(request, user)
                return redirect('teacher')
                #starting session using current user
                # login(request,user)
                # u=request.user
                # print(u.username)
                # print(u.email)
                # print(u.first_name)
                #  return redirect('home')
            else:
                print("Invalid user credentials")
    def get(self, request):
        form_instance = LoginForm()
        return render(request, 'login.html', {'form': form_instance})

from django.contrib.auth import logout

class SignoutView(View):
    def get(self, request):
        logout(request)
        return redirect('signin')
from app1.models import CustomUser
class OtpVerificationView(View):
    def post(self,request):
        otp = request.POST.get('otp')
        try:
            u=CustomUser.objects.get(otp=otp)
            u.is_active=True
            u.is_verified=True
            u.otp=None
            u.save()
            return redirect('signin')
        except:
            # print("Invalid otp")
            messages.error(request,'Invalid otp')
            return redirect('verify_otp')

    def get(self,request):
        return render(request,'otp_verify.html')