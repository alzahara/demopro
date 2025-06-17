from django import forms
from company.models import employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=employee
        fields=['Name','Age','Salary','Designation','Place','image','Department']