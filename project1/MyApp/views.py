from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#home view
def home(request):

    return HttpResponse("Django")

#index view
def index(request):

    return  HttpResponse("Index Page")