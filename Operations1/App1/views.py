from django.shortcuts import render

# Addition
from App1.forms import AdditionForm
def addition(request):
#GET Request
    form_instance=AdditionForm()
    return render(request, 'addition.html',{'form':form_instance})

#factorial
from App1.forms import FactorialForm
def factorial(request):
        form_instance = FactorialForm()
        return render(request, 'factorial.html',{'form':form_instance})


# class ClassName(view):
#     def get(self):
#         #CODE
#     def post(self):
#         # CODE

#BMI calculation
from App1.forms import BmiForm
def bmi(request):
    form_instance = BmiForm()
    return render(request,'bmi.html',{'form':form_instance})

#signup form
from App1.forms import SignupForm
def signup(request):
    form_instance = SignupForm()
    return render(request,'signup.html',{'form':form_instance})

#signup form
# from App1.forms import CalorieForm
# def calorie(request):
#     if request.method=="POST":
#         print(request.POST)
#         return render(request,'calorie.html')
#
#     form_instance = CalorieForm()
#     return render(request,'calorie.html',{'form':form_instance})

from App1.forms import CalorieForm
def calorie(request):
    if request.method=="POST":#After form submission
        print(request.POST)#submitted data
#creating form object using data submitted by user
    form_instance = CalorieForm(request.POST)

    #checks the validity of data using is_valid()
    if form_instance.is_valid():

        #accessing the cleaned data after validation
        data=form_instance.cleaned_data


        weight=data['weight']
        height = data['height']
        print(type('height'))
        age = data['age']
        gender = data['gender']
        activity_level = data['activity_level']
        print(type(activity_level))
        print(weight,height,age,gender,activity_level)

        if(gender=="male"):
            bmr=10*weight+6.25*height-5*age+5 #for man
        else:
            bmr = 10 * weight + 6.25 * height- 5 * age-161 #for women
        c = bmr*float(activity_level)
        print(c)

        return render(request,'calorie.html',{'form': form_instance,'result':c})

    if request.method=="GET":
       form_instance = CalorieForm()
       return render(request, 'calorie.html', {'form': form_instance})
