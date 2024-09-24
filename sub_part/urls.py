from django.urls import path 

from . import views 

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('team',views.team,name='team'),
    path('register',views.register,name='register'),
    path('dashboard',views.dashboard,name='dashboard'),  
]