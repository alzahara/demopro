from django.shortcuts import render

# Addition

def addition(request):
    if(request.method=="POST"):
        print(request.POST)
        n1=request.POST.get('num1')
        n2 = request.POST.get('num2')
        # n1 = request.POST['num1']
        # n2 = request.POST['num2']
        result=int(n1)+int(n2)
        # print(result)
        context={'result':result}
        return render(request, 'addition.html',context)

    return render(request, 'addition.html')

#factorial

def factorial(request):
    if(request.method=="POST"):
        print(request.POST)
        # n1=request.POST.get('num1')
        # n2 = request.POST.get('num2')
        n = int(request.POST['num1'])
        f=1
        for i in range(1,n+1):
            f=f*i
        context={'result':f}
        return render(request, 'factorial.html',context)
    # if (request.method == "GET"):
        return render(request, 'factorial.html')


# class ClassName(view):
#     def get(self):
#         #CODE
#     def post(self):
#         # CODE

#BMI calculation

def bmi(request):
    if request.method=="POST":
        height=float(request.POST.get('height'))
        weight=float(request.POST.get('weight'))
        bmi=weight /(height/100)**2
        context={'bmi':bmi}
        return render(request, 'bmi.html',context)
    return render(request,'bmi.html')


