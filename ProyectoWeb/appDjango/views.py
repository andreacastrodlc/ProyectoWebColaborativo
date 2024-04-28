from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View

from appDjango.forms import ProductoForm, PedidoForm

# Create your views here.

from django.http import HttpResponse

from appDjango.models import  Producto, Pedido, ComponenteProducto, Componente, Contenidopedido


#def index_productos(request):
 #   productos = Producto.objects.order_by('referencia_producto')
  #  context = {'lista_productos': productos}
   # return render(request, 'base.html', context)

class ProductoListView(ListView):
    model = Producto
    template_name = "appDjango/producto_index.html"
    context_object_name = "productos"

def show_producto(request, referencia_producto):
    producto = get_object_or_404(Producto, id=referencia_producto)
    return render(request, 'appDjango/producto_detail.html', {'producto': producto})

class ProductoDetailView(DetailView):
    model = Producto
    #def get_queryset(self):
     #   producto = get_object_or_404(Producto, id=self.kwargs['pk'])
      #  return producto

class ProductoCreateView(View):
    def get(self, request):
        formulario = ProductoForm()
        context = {'formulario': formulario}
        return render(request, 'appDjango/producto_create.html', context)

    def post(self, request):
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_productos')
        return render(request, 'appDjango/producto_create.html', {'formulario': formulario})

def index_pedidos(request):
    pedidos = Pedido.objects.order_by('referencia_pedido')
    context = {'lista_pedidos': pedidos}
    return render(request, 'base.html', context)

class PedidoListView(ListView):
    model = Pedido
    template_name = "appDjango/pedido_index.html"
    context_object_name = "pedidos"

def show_pedido(request, referencia_pedido):
    pedido = get_object_or_404(Pedido, id=referencia_pedido)
    return render(request, 'appDjango/pedido_detail.html', {'pedido': pedido})

class PedidoDetailView(DetailView):
    model = Pedido
    #def get_queryset(self):
     #   producto = get_object_or_404(Producto, id=self.kwargs['pk'])
      #  return producto

class PedidoCreateView(View):
    def get(self, request):
        formulario = PedidoForm()
        context = {'formulario': formulario}
        return render(request, 'appDjango/pedido_create.html', context)

    def post(self, request):
        formulario = PedidoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_pedidos')
        return render(request, 'appDjango/pedido_create.html', {'formulario': formulario})