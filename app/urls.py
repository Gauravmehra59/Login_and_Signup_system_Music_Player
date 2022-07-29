from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("signup_data/",views.signup_data,name="signup_data"),
    path("login_data/",views.login_data,name="login_data"),
]