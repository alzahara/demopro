"""
URL configuration for Company project.

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
from Employee import views


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.employee_list, name='employee_list'),
    path('create/', views.employee_create, name='employee_create'),
    path('employee_details/<int:i>', views.employee_details, name='employee_details'),
    path('delete/<int:i>', views.employee_delete, name='employee_delete'),
    path('edit/<int:i>', views.employee_edit, name='employee_edit'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.employee_list, name='employee_list'),
        path('create/', views.employee_create, name='employee_create'),
        path('employee_details/<int:i>', views.employee_details, name='employee_details'),
        path('delete/<int:i>', views.employee_delete, name='employee_delete'),
        path('edit/<int:i>', views.employee_edit, name='employee_edit'),

    ]
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)