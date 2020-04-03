from django.shortcuts import render
#invoco estas 3 librerias 
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

class LoginClass(View):
    template = 'Login/Login.html'
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            next_url = request.Get.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:Dashboard')
        return render(request,self.template,{})
    
    
    def post(self,request,*args,**kwargs):
        users = request.POST['user']
        password = request.POST['password']
        user = authenticate(username =users, password = password)

        if user is not None:
            login_django(
                request, user
            )
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:Dashboard')
        else:
            self.messege = 'no existe ese usuario o contraseña'
            
        return render(request,self.template,self.get_context())

    def get_context(self):
        return{
            'error':self.messege
        }
    


