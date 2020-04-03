
from django.contrib import admin
from django.urls import  include,path,re_path
from django.contrib.auth.views import logout_then_login
from Login import views #importo o invoco el arhivo
from Landing import views
from Dashboard import views
from Registro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/',include('Registro.urls'), name ='regis'),
    path('Login/',include('Login.urls'), name = 'inicia'), #invoco el url hija
    path('logout/',logout_then_login, name = 'logout'),
    path('',include('Landing.urls'), name = 'landing'),
    path('Dashboard/',include('Dashboard.urls')),
]

