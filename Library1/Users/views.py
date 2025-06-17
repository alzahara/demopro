from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'register.html')

#login view
def login(request):
    return render(request,'login.html')

#logout view
def logout(request):
    return render(request,'logout.html')