from django import  forms
# #form definition
#
# class BookForm(forms.Form):
#     title=forms.CharField(max_length=100)
#     author=forms.CharField(max_length=100)
#     price = forms.IntegerField()
#     language = forms.CharField(max_length=100)
#     pages = forms.IntegerField()
#     image = forms.ImageField()

#Using ModelForm
from Books.models import Book
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        # fields="__all__"
        fields = ['title','author','price','language','pages','image']
