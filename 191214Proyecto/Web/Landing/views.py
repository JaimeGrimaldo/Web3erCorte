from django.shortcuts import render
#invoco estas 3 librerias 
from django.views.generic import View
from django.shortcuts import redirect

#realizo cada clase para html 
class LandingClass(View):
    def get(self,request,*args,**kwargs):
        return render(request,'Landing/landing.html') # retorno la direcion de la carpeta para cada html