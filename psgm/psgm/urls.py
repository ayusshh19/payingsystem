"""psgm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from cgitb import reset
from django.contrib import admin
from django.urls import path

from ayush.views import signup,login_fun,set_room,forget_password,reset_password,password_hist,logout,delete_account,get_room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup),
    path('login/',login_fun),
    path('room/',set_room),
    path('forget/',forget_password),
    path('reset/',reset_password),
    path('history/',password_hist),
    path('logout/',logout),
    path('delete/',delete_account),
    path('room/<int:pk>',get_room)
]
