
from django.db.models import Sum, F # imports que permiten realizar operaciones sobre consultas a la bbdd
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, DeleteView, UpdateView

from appDjango.forms import ProductoForm, PedidoForm, ComponenteForm, ClienteForm

from appDjango.models import Producto, Pedido, ComponenteProducto, Componente, Contenidopedido, Cliente


# VISTAS DE PRODUCTO
# vista para listar productos
class ProductoListView(ListView):
    model = Producto
    template_name = "appDjango/producto_index.html"
    context_object_name = "productos"


# vista de detalle de producto
class ProductoDetailView(DetailView):
    model = Producto


# vista de creacion de producto
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


# vista de eliminacion de producto
class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('index_productos')


# vista de modificacion de producto
class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'appDjango/producto_update.html'
    form_class = ProductoForm

    def get(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        formulario = self.form_class(instance=producto)
        context = {'formulario': formulario, 'producto': producto}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        formulario = self.form_class(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('productos_show', pk=producto.pk)
        else:
            context = {'formulario': formulario, 'producto': producto}
            return render(request, self.template_name, context)


# VISTAS DE PEDIDO
# vista para listar pedidos
class PedidoListView(ListView):
    model = Pedido
    template_name = "appDjango/pedido_index.html"
    context_object_name = "pedidos"


# vista de detalle de pedido, en la que se calcula el precio total del propio pedido, realizado gracias a las fuentes:
# https://stackoverflow.com/questions/53023775/simple-math-on-django-views-with-decimals
# https://docs.djangoproject.com/en/5.0/ref/models/expressions/
class PedidoDetailView(DetailView):
    model = Pedido

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pedido = self.object

        # calcular el precio total del pedido sumando el precio de todos los productos asociados
        precio_total = pedido.contenidopedido_set.annotate(
            precio_total_producto=F('referencia_producto__precio_producto') * F('cantidad_producto')
        ).aggregate(total=Sum('precio_total_producto'))['total']
        pedido.precio_total = precio_total or 0  # si no hay productos asociados precio total=0

        pedido.save()

        return context


# vista de creacion de pedido
class PedidoCreateView(View):
    def get(self, request):
        formulario = PedidoForm()
        context = {'formulario': formulario}
        return render(request, 'appDjango/pedido_create.html', context)

    def post(self, request):
        formulario = PedidoForm(data=request.POST)
        if formulario.is_valid():
            pedido = formulario.save()
            return redirect('pedidos_show', pk=pedido.pk)
        return render(request, 'appDjango/pedido_create.html', {'formulario': formulario})


# vista de modificacion de pedido, unicamente se modifica el cliente y la fecha del pedido
class PedidoUpdateView(UpdateView):
    model = Pedido
    template_name = 'appDjango/pedido_update.html'
    form_class = PedidoForm

    def get(self, request, pk):
        pedido = get_object_or_404(Pedido, pk=pk)
        formulario = self.form_class(instance=pedido)
        context = {'formulario': formulario, 'pedido': pedido}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        pedido = get_object_or_404(Pedido, pk=pk)
        formulario = self.form_class(request.POST, instance=pedido)
        if formulario.is_valid():
            formulario.save()
            return redirect('pedidos_show', pk=pedido.pk)
        else:
            context = {'formulario': formulario, 'pedido': pedido}
            return render(request, self.template_name, context)


# VISTAS DE COMPONENTE
# vista para listar componentes
class ComponenteListView(ListView):
    model = Componente
    template_name = "appDjango/componente_index.html"
    context_object_name = "componentes"


# vista de detalle de componente
class ComponenteDetailView(DetailView):
    model = Componente


# vista de creacion de componente
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


# VISTAS DE CLIENTE
# vista para listar clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = "appDjango/cliente_index.html"
    context_object_name = "clientes"


# vista de detalle de cliente
class ClienteDetailView(DetailView):
    model = Cliente


# vista para crear cliente
class ClienteCreateView(View):
    def get(self, request):
        formulario = ClienteForm()
        context = {'formulario': formulario}
        return render(request, 'appDjango/cliente_create.html', context)

    def post(self, request):
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            nuevo_cliente = formulario.save()
            return redirect('clientes_show', pk=nuevo_cliente.pk)
        return render(request, 'appDjango/cliente_create.html', {'formulario': formulario})


# vista para eliminar cliente
class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('index_clientes')


# vista para modificar datos de un cliente
class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'appDjango/cliente_update.html'
    form_class = ClienteForm

    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        formulario = self.form_class(instance=cliente)
        context = {'formulario': formulario, 'cliente': cliente}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        formulario = self.form_class(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('clientes_show', pk=cliente.pk)
        else:
            context = {'formulario': formulario, 'cliente': cliente}
            return render(request, self.template_name, context)


# VISTAS CON FUNCIONES ESPECIFICAS
# vista para asignar componentes a un producto en especifico
def asignar_componentes_producto(request, pk):
    # se obtiene el objeto del producto al que vamos a anadir componentes
    producto = get_object_or_404(Producto, pk=pk)

    # si se envia el formulario:
    if request.method == 'POST':
        # se obtiene una lista de los IDs de los componentes seleccionados
        componentes_seleccionados = request.POST.getlist('componentes')

        # iteracion sobre los ID de los componentes seleccionados
        for componente_id in componentes_seleccionados:
            componente = get_object_or_404(Componente, pk=componente_id)
            # creacion y guardado de un nuevo componente_producto
            componenteproducto = ComponenteProducto(referencia_producto=producto, referencia_componente=componente)
            componenteproducto.save()

    componentes = Componente.objects.all()
    componentes_asignados = producto.componenteproducto_set.all()

    context = {'producto': producto, 'componentes': componentes, 'componentes_asignados': componentes_asignados}
    return render(request, 'appDjango/asignar_componentes_producto.html', context)


# vista para asignar productos a un pedido
def asignar_productos_pedido(request, pk_pedido):
    pedido = get_object_or_404(Pedido, pk=pk_pedido)

# si se envia el formulario:
    if request.method == 'POST':
        # obtener producto y cantidad introducida
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad', 0))

        if producto_id and cantidad > 0:
            producto = get_object_or_404(Producto, pk=producto_id)

            # crear un objeto contenido pedido nuevo con los datos obtenidos a traves del formulario
            Contenidopedido.objects.create(referencia_pedido=pedido, referencia_producto=producto,
                                           cantidad_producto=cantidad)
            return redirect('pedidos_show', pk=pk_pedido)

    productos = Producto.objects.all()
    context = {'pedido': pedido, 'productos': productos}
    return render(request, 'appDjango/asignar_productos_pedido.html', context)


# vista para eliminar productos de un pedido
class EliminarProductoPedidoView(View):
    def post(self, request, pk_pedido):
        producto_pedido_id = request.POST.get('producto_pedido_id')
        contenido_producto = get_object_or_404(Contenidopedido, pk=producto_pedido_id)
        contenido_producto.delete()
        return redirect('pedidos_show', pk=pk_pedido)
