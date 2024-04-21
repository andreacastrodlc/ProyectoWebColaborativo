from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('componente/<int:referencia_componente>', views.componente, name='detail')

]