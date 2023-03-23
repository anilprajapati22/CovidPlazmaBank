from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('',views.home,name='home'),
    path("register", views.register, name="register"),
    path("Requester", views.Requester, name="Requester"),
    path("RequesterBloodIsAvailable", views.RequesterBloodIsAvailable, name="RequesterBloodIsAvailable"),
    path("Donner", views.Donner, name="Donner"),
    path("BankAdminPage", views.BankAdminPage, name="BankAdminPage"),
    path("BankAdminPageHistory", views.BankAdminPageHistory, name='BankAdminPageHistory'),
    path("is_donner_already_donated", views.is_donner_already_donated, name="is_donner_already_donated"),    
]