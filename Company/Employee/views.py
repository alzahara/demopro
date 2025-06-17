from django.shortcuts import render,redirect

# Create your views here.
#employee_list view
from Employee.models import Employee
def employee_list(request):
    e=Employee.objects.all()
    return render(request,'employee_list.html',{'employee':e})

#employee_create view
from Employee.forms import EmployeeForm
def employee_create(request):
    if(request.method=="POST"):
        form_instance=EmployeeForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('employee_list')
    form_instance=EmployeeForm()
    return render(request,'employee_create.html',{'form':form_instance})

#employee_details view

def employee_details(request,i):
    e = Employee.objects.get(id=i)
    return render(request, 'employee_details.html', {'employee': e})

#employee_delete view

def employee_delete(request,i):
    e = Employee.objects.get(id=i)
    e.delete()
    return redirect('employee_list')

#employee_edit view

def employee_edit(request,i):
    e = Employee.objects.get(id=i)
    if(request.method=="POST"):
        form_instance=EmployeeForm(request.POST,request.FILES,instance=e)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('employee_list')

    form_instance=EmployeeForm(instance=e)
    return render(request, 'employee_edit.html', {'form': form_instance})






