from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('choice',views.choice,name='choice'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('teams',views.teams,name='teams'),
    
]