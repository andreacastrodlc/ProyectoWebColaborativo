from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from appDjango.models import Componente


def index(request):
    componentes = Componente.objects.order_by('marca_componente')
    output = ', '.join([d.marca_componente for d in componentes])
    return HttpResponse(output) #primera vista de prueba que muestra las marcas de todos los componentes separados por comas

def detail(request, referencia_componente):
    componentes = Componente.objects.get(pk=referencia_componente)
    return HttpResponse(componentes)