from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
from .forms import SignupForm
class SignupView(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')

    def get(self, request):
        return render(request,'signup.html')

