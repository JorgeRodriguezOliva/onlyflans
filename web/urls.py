from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.indice, name="indice"),
    path('acerca', views.acerca, name="acerca"),
    path('bienvenido', views.bienvenido, name="bienvenido"),
    path('exito', views.exito, name="exito"),
    path('contacto', views.contacto, name="contacto"),
    path('detalle/<uuid:flan_uuid>', views.detalle, name='detalle'),
    path('profile/', views.profile_view, name='profile'),
    path('profile_exito', views.profile_exito, name='profile_exito'),
    path('register/', views.register, name='register'),
    path('profile_e/', views.profile_e, name='profile_e'),
]


