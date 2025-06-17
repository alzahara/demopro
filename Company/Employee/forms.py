from django import forms
from Employee.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['name','age','salary','designation','place','image','department_name']