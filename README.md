Link del repositorio: https://github.com/andreacastrodlc/ProyectoWebColaborativo

# Nuestras urls
A continuación mostramos todas nuestras urls
```
urlpatterns = [
    # urls para productos
    path('productos/', ProductoListView.as_view(), name='index_productos'),
    path('productos/<int:pk>', ProductoDetailView.as_view(), name='productos_show'),
    path('productos/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_delete'),
    path('productos/modificar/<int:pk>', ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/create', ProductoCreateView.as_view(), name='producto_create'),
    # urls para clientes
    path('clientes/', ClienteListView.as_view(), name='index_clientes'),
    path('clientes/<int:pk>', ClienteDetailView.as_view(), name='clientes_show'),
    path('clientes/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
    path('clientes/modificar/<int:pk>', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/create', ClienteCreateView.as_view(), name='cliente_create'),
    # urls para pedidos
    path('pedidos/', PedidoListView.as_view(), name='index_pedidos'),
    path('pedidos/<int:pk>', PedidoDetailView.as_view(), name='pedidos_show'),
    path('pedidos/create', PedidoCreateView.as_view(), name='pedido_create'),
    path('pedidos/modificar/<int:pk>', PedidoUpdateView.as_view(), name='pedido_update'),
    # urls para componentes
    path('componentes/', ComponenteListView.as_view(), name='index_componentes'),
    path('componentes/<int:pk>', ComponenteDetailView.as_view(), name='componente_show'),
    path('componentes/create', ComponenteCreateView.as_view(), name='componente_create'),
    # urls para asignar/eliminar relaciones a entidades
    path('productos/<int:pk>/asignar_componentes/', asignar_componentes_producto, name='asignar_componentes_producto'),
    path('asignar_productos_pedido/<int:pk_pedido>', asignar_productos_pedido, name='asignar_productos_pedido'),
    path('pedidos/eliminar_producto/<int:pk_pedido>/', EliminarProductoPedidoView.as_view(),
         name='eliminar_producto_pedido')
]
```
# Implementaciones extras añadidas.
Además de lo requerido en el enunciado se han implementado las siguientes funcionalidades: 
-Gestión de los componentes que componen cada producto, se accede a través de la vista de detalle de cada producto.
- Gestión de clientes
- Asignación de componentes a productos
- Asignación de productos a pedidos
- Eliminación de un producto específico en un pedido

#Clase para ver los detalles del producto en el views.py
```
class ProductoDetailView(DetailView):
    model = Producto
```

Views.py-> asignar componentes al producto
```
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
```

Asignación componentes a productos
HTML
```
{% extends 'base.html' %}
{% block contenido %}
    <h2>Asignar componentes a producto: {{ producto.nombre_producto }}</h2>

    <form method="post">
        {% csrf_token %}
        <label for="componentes">Componentes disponibles:</label>
        <select name="componentes" multiple> <!--multiple para que se puedan escoger mas de 1 componente-->
            {% for componente in componentes %}
                <option value="{{ componente.pk }}">{{ componente.modelo_componente }}</option><!--valor que se obtiene pk de componente y valor visible el modelo del componente-->
            {% endfor %}
        </select>
        <input type="submit" value="Asignar componentes">
    </form>
    <h3>
        {% if componentes_asignados %}
            Componentes asignados:
        {% else %}
            Este producto no tiene componentes asignados.
        {% endif %}
    </h3>
    <ul>
        {% for componente_asignado in componentes_asignados %}
            <li>{{ componente_asignado.referencia_componente.modelo_componente }}</li><!--muestra el modelo de los componentes que el producto tiene asignado-->
        {% endfor %}
    </ul>
{% endblock %}
```
Vista
```
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
```

Cada componente puede ser asignado
varias veces a un producto ya que hay productos que tienen el mismo componente varias veces, p. ej. un coche tiene 4 ruedas.
```
 <select name="componentes" multiple>
```

Asignación productos a un pedido
```
HTML
{% extends 'base.html' %}
{% block contenido %}
<form method="post">
    {% csrf_token %}
    <label for="producto_id">Producto:</label>
    <select name="producto_id" required>
        <option value="">Seleccione un producto</option>
        {% for producto in productos %}
            <option value="{{ producto.pk }}">{{ producto.nombre_producto }}</option>
        {% endfor %}
    </select><br>

    <label for="cantidad">Cantidad:</label>
    <input type="number" name="cantidad" min="1" value="1" required><br>

    <input type="submit" value="Asignar producto">
</form>
{% endblock %}
```
Vista
```
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
```

Eliminación de un producto específico en un pedido
```
class EliminarProductoPedidoView(View):
    def post(self, request, pk_pedido):
        producto_pedido_id = request.POST.get('producto_pedido_id')
        contenido_producto = get_object_or_404(Contenidopedido, pk=producto_pedido_id)
        contenido_producto.delete()
        return redirect('pedidos_show', pk=pk_pedido)
```
# Implementaciones no operativas o con errores especificadas si las hubiera.



# Documentacion extra de ayuda.

