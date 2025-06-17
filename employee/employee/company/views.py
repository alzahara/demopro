from django.shortcuts import render,redirect

def home(request):
    return render(request,'home.html')

from company.forms import EmployeeForm
def addemployee(request):
    if (request.method=='POST'):
        form_instance=EmployeeForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('employeelist')
    form_instance=EmployeeForm()
    return render(request, 'addemployee.html', {'form': form_instance})

from company.models import employee
def employeelist(request):
    e=employee.objects.all()
    print(e)
    return render(request,'employeelist.html',{'employees':e})


def detail(request,i):
    e=employee.objects.get(id=i)
    return render(request, 'detail.html', {'employee': e})

def edit(request,i):
    e=employee.objects.get(id=i)
    if (request.method=='POST'):
        form_instance=EmployeeForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('employeelist')
    form_instance=EmployeeForm(instance=e)
    return render(request, 'addemployee.html', {'form': form_instance})

def delete(request,i):
    e=employee.objects.get(id=i)
    e.delete()
    return redirect('company:employeelist')