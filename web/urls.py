from django.urls import path

from . import views 

urlpatterns = [
    path('', views.hola_template),
    path('text/', views.hola_text),
    path('json/', views.hola_json),
]