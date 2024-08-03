from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse


def saludar_function(request):
    return HttpResponse("Hola MUNDO!!!")

# Create your views here.
def hola(req):
    return HttpResponse("INICIO APP")

def hola_text(req):
    return HttpResponse("Bienvenidos")

def hola_json(req):
    data = {
        "message": "HULK!!!"
    }
    return JsonResponse(data)

def hola_template(req):
    context = {
        "message": "Bienvenidos a utilizar un template dinámico con Only Flans!!!"
    }
    return render(req, 'index.html', context)

