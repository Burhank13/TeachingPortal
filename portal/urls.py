from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('choice',views.choice,name='choice'),
    path('login',views.login,name='login'),
    path('choseProfession',views.choseProfession,name='choseProfession'),
    
]