from django.shortcuts import render,redirect

#Home

def home(request):
    return render(request,'home.html')

#Addbook
#user deffinED FORM VIEW
from Books.models import Book

def Addbook(request):
    if (request.method == 'POST'):
        # print(request.POST)
        # print(request.FILES)

        t = request.POST['t']
        a = request.POST['a']
        n = request.POST['n']
        l = request.POST['l']
        p = request.POST['p']
        i = request.FILES['i']
        b=Book.objects.create(title=t,author=a,price=n,language=l,pages=p,image=i)
        b.save()
        return redirect('Books:viewbook')
    return render(request,'addbook.html')

#Addbook1
#build in form view
from Books.forms import BookForm
def Addbook1(request):
    if (request.method == 'POST'):
        # print(request.POST)
        # print(request.FILES)

        form_instance=BookForm(request.POST,request.FILES)
        if form_instance.is_valid():
            # data=form_instance.cleaned_data
            # print(data)
            # t = data['title']
            # a = data['author']
            # n = data['price']
            # l = data['language']
            # p = data['pages']
            # b = Book.objects.create(title=t, author=a, price=n, language=l, pages=p)
            #optimised way
            # b = Book.objects.create(title=form_instance.cleaned_data['title'], author=form_instance.cleaned_data['author'], price=form_instance.cleaned_data['price'], language=form_instance.cleaned_data['language'], pages=form_instance.cleaned_data['pages'],image=form_instance.cleaned_data['image'])
            # b.save()

        #model form class using
            form_instance.save()
            #redirect(pathname)
        # return redirect('Books:home')
        return redirect('Books:viewbook')

    if(request.method=='GET'):
      form_instance=BookForm()
      return render(request,'addbook1.html',{'form':form_instance})

#Viewbook

def Viewbook(request):
    b=Book.objects.all()
    print(b)
    return render(request,'viewbook.html',{'books':b})


#Detail View
def bookdetail(request,i):
    # id=2
    # # print(i)
    # b=Book.objects.get(id=id)

    # print(i)
    b = Book.objects.get(id=i)
    return render(request,'detail.html',{'book':b})

#Edit View
def editbook(request,i):
    b = Book.objects.get(id=i)
    if(request.method=="POST"):
        form_instance=BookForm(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('Books:viewbook')

    b = Book.objects.get(id=i)
    form_instance=BookForm(instance=b)
    return render(request,'editbook.html',{'form':form_instance})

#Delete View
def deletebook(request,i):

    b = Book.objects.get(id=i)
    b.delete()
    return redirect('Books:viewbook')

#search view
from django.db.models import Q
def searchbooks(request):
    if(request.method=="POST"):
        print('hello')
        data=request.POST['q']
        print(data)
        b=Book.objects.filter(Q(title__contains=data) | Q(author__contains=data) |Q(language__contains=data))
        #filter condition to read two or more records from a table

        #Qobject to use logical and/or/not syntax in ORM Queries.

        #Django lookups{fieldname__lookuo)(eg:age__gt)
        print(b)
        context={'Book':b}
        return render(request, 'search.html',context)
    return render(request, 'search.html')

