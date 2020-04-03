#estos 3 libreria se necesita 
from django.urls import include,re_path,path
from django.conf import settings 
from . import views 
#importo el archivo 

from Login.views import LoginClass

  
app_name = 'Login'

urlpatterns = [
    path('',LoginClass.as_view(),name='Login'), #llamo las url que va a tener cada html en las hijas
]