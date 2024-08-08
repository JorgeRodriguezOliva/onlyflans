from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def home(req):
    context = {
        "message": "Bienvenidos a Only Flans",
        "user": {"username": "Jorge", "password": 1234, "is_active": False},
        "productos": [{"name": "postre_1", "url": "/static/img/foto1.jpg"},
                      {"name": "postre_2", "url": "/static/img/foto2.jpg"},
                      {"name": "postre_3", "url": "/static/img/foto3.jpg"},
                      {"name": "postre_4", "url": "/static/img/foto4.jpg"},
            {"name": "postre_5", "url": "/static/img/foto5.jpg"},
            {"name": "postre_6", "url": "/static/img/foto6.jpg"},
            {"name": "postre_7", "url": "/static/img/foto7.jpg"},
            {"name": "postre_8", "url": "/static/img/foto8.jpg"},
            {"name": "postre_9", "url": "/static/img/foto9.jpg"}
        ]
    }
    return render(req, 'index.html', context)


def acerca(req):
    contex = {
        "data": "Acerca de nosotros"
    }
    return render(req, 'about.html', contex)

def bienvenido(req):
    contex = {
        "data": "Bienvenido"
    }
    return render(req, 'welcome.html', contex)

