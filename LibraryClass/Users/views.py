from django.shortcuts import render,redirect

# Register View

def register(request):
    return render(request,'register.html')


#login view
def login(request):
    return render(request,'login.html')

#logout view
def logout(request):
    return render(request,'logout.html')