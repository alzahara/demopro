from django.shortcuts import render

#Home

def home(request):
    return render(request,'home.html')

#Addbook

def Addbook(request):
    return render(request,'addbook.html')

#Viewbook

def Viewbook(request):
    return render(request,'viewbook.html')