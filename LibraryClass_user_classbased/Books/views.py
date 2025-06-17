from django.shortcuts import render,redirect

# #Home
#
# def home(request):
#     return render(request,'home.html')
from django.views import View
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home.html')
#Addbook
#user deffinED FORM VIEW
from Books.models import Book

# def Addbook(request):
#     if (request.method == 'POST'):
#         # print(request.POST)
#         # print(request.FILES)
#
#         t = request.POST['t']
#         a = request.POST['a']
#         n = request.POST['n']
#         l = request.POST['l']
#         p = request.POST['p']
#         i = request.FILES['i']
#         b=Book.objects.create(title=t,author=a,price=n,language=l,pages=p,image=i)
#         b.save()
#         return redirect('Books:viewbook')
#     return render(request,'addbook.html')

#class based
class AddBookView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'addbook.html')

    def post(self, request, *args, **kwargs):
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

#Addbook1
#build in form view
from Books.forms import BookForm
# def Addbook1(request):
#     if (request.method == 'POST'):
#         # print(request.POST)
#         # print(request.FILES)
#
#         form_instance=BookForm(request.POST,request.FILES)
#         if form_instance.is_valid():
#             # data=form_instance.cleaned_data
#             # print(data)
#             # t = data['title']
#             # a = data['author']
#             # n = data['price']
#             # l = data['language']
#             # p = data['pages']
#             # b = Book.objects.create(title=t, author=a, price=n, language=l, pages=p)
#             #optimised way
#             # b = Book.objects.create(title=form_instance.cleaned_data['title'], author=form_instance.cleaned_data['author'], price=form_instance.cleaned_data['price'], language=form_instance.cleaned_data['language'], pages=form_instance.cleaned_data['pages'],image=form_instance.cleaned_data['image'])
#             # b.save()
#
#         #model form class using
#             form_instance.save()
#             #redirect(pathname)
#         # return redirect('Books:home')
#         return redirect('Books:viewbook')
#
#     if(request.method=='GET'):
#       form_instance=BookForm()
#       return render(request,'addbook1.html',{'form':form_instance})


#class based view

class AddBookView1(View):
    def get(self, request, *args, **kwargs):
        form_instance = BookForm()
        return render(request, 'addbook1.html', {'form': form_instance})
    def post(self, request, *args, **kwargs):
        form_instance=BookForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('Books:viewbook')
#Viewbook

class ViewBook(View):
    def get(self, request, *args, **kwargs):
        b=Book.objects.all()
        # print(b)
        return render(request,'viewbook.html',{'books':b})


#Detail View
# def bookdetail(request,i):
#     # id=2
#     # # print(i)
#     # b=Book.objects.get(id=id)
#
#     # print(i)
#     b = Book.objects.get(id=i)
#     return render(request,'detail.html',{'book':b})

class BookDetailView(View):
    def get(self, request,i):
        b = Book.objects.get(id=i)
        return render(request, 'detail.html', {'book': b})

#Edit View
# def editbook(request,i):
#     b = Book.objects.get(id=i)
#     if(request.method=="POST"):
#         form_instance=BookForm(request.POST,request.FILES,instance=b)
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('Books:viewbook')

    # b = Book.objects.get(id=i)
    # form_instance=BookForm(instance=b)
    # return render(request,'editbook.html',{'form':form_instance})

class EditBookView(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        form_instance = BookForm(instance=b)
        return render(request, 'editbook.html', {'form': form_instance})
    def post(self,request,i):
        b = Book.objects.get(id=i)
        form_instance = BookForm(request.POST, request.FILES, instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('Books:viewbook')

#Delete View
# def deletebook(request,i):
#
#     b = Book.objects.get(id=i)
#     b.delete()
#     return redirect('Books:viewbook')

class DeleteBookView(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        b.delete()
        return redirect('Books:viewbook')

#search view
# def searchbooks(request):
#     if(request.method=="POST"):
#         data=request.POST['q']
#         print(data)
#         return render(request,'search.html')
#     return render(request, 'search.html')
from django.db.models import Q
class SearchBookView(View):
    def get(self, request):
        return render(request, 'search.html')
    def post(self,request):
        data=request.POST['q']
        print(data)
        b=Book.objects.filter(Q(title__contains=data) | Q(author__contains=data) | Q(language__contains=data))
        print(b)
        context={'Book':b}
        return render(request,'search.html',context)

