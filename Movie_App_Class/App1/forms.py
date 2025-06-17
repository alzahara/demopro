from django import  forms
from App1.models import Movie
#form definition

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['movie_name','description','director_name','language','year','image']
