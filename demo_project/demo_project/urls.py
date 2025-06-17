"""
URL configuration for demo_project project.

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
from App2 import views
from App1 import views as view1#alaising (onE METHOD FOR MULTILE APPS)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',view1.home,name="home"),#http://127.0.0.1:8000/
    path('first', view1.first, name="first"),#http://127.0.0.1:8000/first
    path('second', view1.second, name="second"),#http://127.0.0.1:8000/second
    path('third', views.third, name="third"),#http://127.0.0.1:8000/third
    path('fourth', views.fourth, name="fourth"),#http://127.0.0.1:8000/fourth
]
