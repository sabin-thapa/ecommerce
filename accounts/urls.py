from django.contrib import admin
from django.urls import path
from . import views

app_name: 'accounts'

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutPage, name="logout"),

]
