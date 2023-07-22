"""
URL configuration for employmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from . import views
from employapp.models import *

urlpatterns = [
    
    path('',views.home , name="home"),
    path("login/",views.login1, name="login"),
    path("logout/",views.logout1,name="logout"),
    path("register/",views.register,name="register"),
    path("add_details/", views.add_details,name="add_details"),
    path("remove_details/", views.remove_details,name="remove_details"),
    path("remove_details/<int:emp_id>", views.remove_details,name="remove_details"),
    path("view_details/", views.view_details,name="view_details"),
    path("filter_details/", views.filter_details,name="filter_details"),
    path("forgot_password/",views.forgot_password,name="forgot_password"),
    path("change_password/<token>",views.change_password,name="change_password"),
    
]
