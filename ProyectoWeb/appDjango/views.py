from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View

from appDjango.forms import ProductoForm, PedidoForm, ComponenteForm

# Create your views here.


from appDjango.models import Producto, Pedido, ComponenteProducto, Componente


class ProductoListView(ListView):
    model = Producto
    template_name = "appDjango/producto_index.html"
    context_object_name = "productos"


class ProductoDetailView(DetailView):
    model = Producto


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


class PedidoListView(ListView):
    model = Pedido
    template_name = "appDjango/pedido_index.html"
    context_object_name = "pedidos"


class PedidoDetailView(DetailView):
    model = Pedido


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


class ComponenteListView(ListView):
    model = Componente
    template_name = "appDjango/componente_index.html"
    context_object_name = "componentes"


class ComponenteDetailView(DetailView):
    model = Componente


class ComponenteCreateView(View):
    def get(self, request):
        formulario = ComponenteForm()
        context = {'formulario': formulario}
        return render(request, 'appDjango/componente_create.html', context)

    def post(self, request):
        formulario = ComponenteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_componentes')
        return render(request, 'appDjango/componente_create.html', {'formulario': formulario})


def asignar_componentes_producto(request, pk):
    #se obtiene el objeto del producto al que vamos a anadir componentes
    producto = get_object_or_404(Producto, pk=pk)

    #si se envia el formulario:
    if request.method == 'POST':
        #se obtiene una lista de los IDs de los componentes seleccionados
        componentes_seleccionados = request.POST.getlist('componentes')

        #iteracion sobre los ID de los componentes seleccionados
        for componente_id in componentes_seleccionados:
            componente = get_object_or_404(Componente, pk=componente_id)
            #creacion y guardado de un nuevo componente_producto
            componenteproducto = ComponenteProducto(referencia_producto=producto, referencia_componente=componente)
            componenteproducto.save()

    componentes = Componente.objects.all()
    componentes_asignados = producto.componenteproducto_set.all()

    context = {'producto': producto, 'componentes': componentes, 'componentes_asignados': componentes_asignados}
    return render(request, 'appDjango/asignar_componentes_producto.html', context)
