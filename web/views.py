from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm, ContactModelForm
from django.contrib.auth.decorators import login_required

def indice(req):
    flanes_all = Flan.objects.all()
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {"user": {"username": "Jorge", "password": 1234, "is_active": False},
            "flanes_publicos": flanes_publicos,
            "flanes_all": flanes_all,
            }
    return render(req, 'index.html', context)


def acerca(req):
    contex = {
        "data": "Acerca de nosotros"
    }
    return render(req, 'about.html', contex)

@login_required
def bienvenido(req):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(req, 'welcome.html', {"flanes_privados": flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST) 
        if form.is_valid():
            ContactForm.objects.create(**form.cleaned_data) 
            return HttpResponseRedirect('/exito')
    else: 
        form = ContactModelForm()    
    return render(request, 'contactus.html', {'form':form})

def exclusivos(req):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(req, 'exclusivos.html', {"flanes_privados": flanes_privados})

def exito(request):
    return render(request, 'success.html', {})

