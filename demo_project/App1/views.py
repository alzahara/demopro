from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#home view
def home(request):

    context={'name':'Alzahara','age':26,'place':'Ernakulam'}
    return render(request,'home.html',context)

    # return HttpResponse("Welcome to Home")

#first view
def first(request):
    return render(request,'first.html')

    # return HttpResponse("First Page")

#second view
def second(request):
    return render(request,'second.html')

    # return HttpResponse("Second Page")

