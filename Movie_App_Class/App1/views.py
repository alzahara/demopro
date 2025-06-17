from django.shortcuts import render,redirect
from django.urls import reverse_lazy

# from App1.models import Movie
# listview
# def movielist(request):
#     m=Movie.objects.all()
#     return render(request,'movielist.html',{'movies':m})

#using Listview class
from App1.models import Movie
from django.views.generic import ListView
class MovieList(ListView):
    model = Movie
    template_name = 'movielist.html'
    context_object_name = 'movies'


# from App1.forms import MovieForm
# addmovie
# def addmovie(request):
#     if(request.method=="POST"):
#         form_instance=MovieForm(request.POST,request.FILES)
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('movielist')
#
#     form_instance=MovieForm()
#     return render(request,'addmovie.html',{'form': form_instance})

from App1.forms import MovieForm
from django.views.generic import CreateView

class AddMovie(CreateView):
    form_class = MovieForm
    template_name = 'addmovie.html'
    model = Movie
    success_url = reverse_lazy('movielist')
#detailview

# def moviedetail(request,i):
#     m=Movie.objects.get(id=i)
#     return render(request,'moviedetail.html',{'movie':m})
from django.views.generic import DetailView
class MovieDetail(DetailView):
    model = Movie
    template_name = 'moviedetail.html'
    context_object_name = 'movie'

#deletemovie

# def deletemovie(request,i):
#     m = Movie.objects.get(id=i)
#     m.delete()
#     return redirect('movielist')
from django.views.generic import DeleteView
class DeleteMovie(DeleteView):
    model = Movie
    template_name = "delete.html"#extra add this for deleteView class
    success_url = reverse_lazy('movielist')

#editmovie

# def editmovie(request,i):
#     m = Movie.objects.get(id=i)
#     if (request.method == "POST"):
#         form_instance = MovieForm(request.POST, request.FILES,instance=m)
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('movielist')
#
#     form_instance=MovieForm(instance=m)
#     return render(request, 'editmovie.html', {'form': form_instance})

from django.views.generic import UpdateView
class EditMovie(UpdateView):
    form_class = MovieForm
    template_name = 'editmovie.html'
    model = Movie
    success_url = reverse_lazy('movielist')



