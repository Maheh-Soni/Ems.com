from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('AdminLogin',AdminLogin,name="AdminLogin"),
    path('AdminRegistration/',AdminRegistration,name="AdminRegistration"),
    path('UserLogin',UserLogin,name="UserLogin"),
    path('UserRegistration/',UserRegistration,name="UserRegistration"), 
    path('Userpage/',Userpage,name="Userpage"), 
    path('showdata/',showdata,name="showdata"),
    path('Userdelete/<int:id>/',Userdelete,name="Userdelete"),
    path('Userupdate/<int:id>/',Userupdate,name="Userupdate"),
]
