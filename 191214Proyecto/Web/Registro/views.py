

from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from .forms import RegisterBusinessForm

class RegistrateView(FormView):
  
    template_name = 'Registro/Registro.html'
        
    # GET
    def get(self, request, *args, **kwargs):
        print("SI ENTOR A REGISTRATEVIEW get")
        form = RegisterBusinessForm(request.GET or None)
        context = {
            'form_get' : form
        }
        return render(request, self.template_name, context)

    # POST
    def post(self, request, *args, **kwargs):
        print("SI ENTRO AL POST")
        formok = RegisterBusinessForm(request.POST or None )
        print(formok)
        print("SI ENTRO A POST")
        if formok.is_valid():
            print("SI ENTO AL IF")
            self.object = formok.save(commit = False)
            self.object.set_password(self.object.password)
            print("LLEGO ANTES DEL SAVE")
            self.object.save()
            print("PASE EL SABE")
        return redirect('Login:Login')
