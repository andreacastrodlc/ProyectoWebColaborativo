from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, DeleteView

from appDjango.forms import ProductoForm

# Create your views here.

from django.http import HttpResponse

from appDjango.models import  Producto


def index_productos(request):
    productos = Producto.objects.order_by('referencia_producto')
    context = {'lista_productos': productos}
    return render(request, 'base.html', context)

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
    #    producto = get_object_or_404(Producto, id=self.kwargs['pk'])
    #    return producto

class ProductoCreateView(View):
    def get(self, request):
        formulario = ProductoForm()
        context = {'formulario': formulario}
        return render(request, 'appDjango/producto_create.html', context)

    def post(self, request):
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
        return render(request, 'appDjango/producto_create.html', {'formulario': formulario})


class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('index') #configuramos en caso de que el delete se haya producido, a dónde se redirigirá, en este caso el index


class ProductoUpdateView(UpdateView):
    model = Producto

    def get(self, request, pk):
        producto = Producto.objects.get(id=pk)
        formulario = ProductoForm(instance=producto)
        context = {
            'formulario': formulario,
            'producto': producto

        }
        return render(request, self.template_name, 'appDjango/producto_update.html/')
        producto = Producto.objects.get(id=pk)
        formulario = ProductoForm(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
        else:
            formulario= ProductoForm(instance=producto)
        return render(request, self.template_name, 'appDjango/producto_update.html')