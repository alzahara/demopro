"""
URL configuration for Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Books import views
app_name="Books"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(),name="home"),
    # path('', views.home,name="home"),#http:127.0.0.1:8000
    # path('addbook', views.Addbook,name="addbook"),#http:127.0.0.1:8000\addbook
    path('addbook', views.AddBookView.as_view(), name="addbook"),
    path('addbook1', views.AddBookView1.as_view(), name="addbook1"),
    # path('addbook1', views.Addbook1,name="addbook1"),
    # path('viewbook', views.Viewbook, name="viewbook"),#http:127.0.0.1:8000\viewbook
    path('viewbook', views.ViewBook.as_view(), name="viewbook"),
    # path('bookdetail/<int:i>', views.bookdetail, name="bookdetail"),
    path('bookdetail/<int:i>', views.BookDetailView.as_view(), name="bookdetail"),

    # path('editbook/<int:i>', views.editbook, name="editbook"),
    path('editbook/<int:i>', views.EditBookView.as_view(), name="editbook"),

    # path('deletebook/<int:i>', views.deletebook, name="deletebook"),
    path('deletebook/<int:i>', views.DeleteBookView.as_view(), name="deletebook"),

    path('searchbooks', views.SearchBookView.as_view(), name="searchbooks"),
    # path('searchbooks', views.searchbooks, name="searchbooks"),
]

