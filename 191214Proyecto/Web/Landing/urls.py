#estos 3 libreria se necesita 
from django.urls import include,re_path,path
from django.conf import settings 
from . import views 
#importo el archivo 
from django.contrib.auth import views as auth_view
from Landing.views import LandingClass

  
app_name = 'Landing'

urlpatterns = [
    path('',LandingClass.as_view(), name='Landing'),
]