from django.shortcuts import render,redirect

from App1.models import Movie
# listview
def movielist(request):
    m=Movie.objects.all()
    return render(request,'movielist.html',{'movies':m})

from App1.forms import MovieForm
# addmovie
def addmovie(request):
    if(request.method=="POST"):
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('movielist')

    form_instance=MovieForm()
    return render(request,'addmovie.html',{'form': form_instance})

#detailview

def moviedetail(request,i):
    m=Movie.objects.get(id=i)
    return render(request,'moviedetail.html',{'movie':m})

#deletemovie

def deletemovie(request,i):
    m = Movie.objects.get(id=i)
    m.delete()
    return redirect('movielist')

#editmovie

def editmovie(request,i):
    m = Movie.objects.get(id=i)
    if (request.method == "POST"):
        form_instance = MovieForm(request.POST, request.FILES,instance=m)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('movielist')

    form_instance=MovieForm(instance=m)
    return render(request, 'editmovie.html', {'form': form_instance})


