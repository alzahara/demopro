from person.models import Person
class SignupForm(forms.ModelForm):
    class Meta:
        model=Person
        # fields="__all__"
        fields = ['username','password','age','place','image','address']