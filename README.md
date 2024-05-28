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
         name='eliminar_producto_pedido'),
    # urls de sesion
    path('login/', login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.logout_view, name='logout'),

    # url envio emails
    path('soporte/', views.enviar_mensaje_soporte, name='soporte'),
    path('actualizar_estado_pedido/<int:pk>/', views.actualizar_estado_pedido, name='actualizar_estado_pedido')
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

# Funcionalidades JavaScript
Se han implementado las siguientes funcionalidades de JS:
1- Aumento/ disminución tamaño texto
    Para modificar el tamaño de la página se han añadido dos botones a la plantilla base para que extienda sobre el resto:

```
<button id="btn-aumentar">🔎➕</button>
        <button id="btn-disminuir">🔎➖</button>
```
En el archivo de JavaScript hemos añadido un EventListener para cuando el documento HTML esté cargado, asegurando que el código se ejecute después de que todos los elementos del DOM estén disponibles.
Seleccionamos  los botones de aumentar y disminuir el tamaño del texto utilizando sus IDs. 
Al hacer clic en el botón "Aumentar", se seleccionan todos los elementos h1, h2 y p en la página, se obtiene su tamaño de fuente actual y se incrementa en un 20% (* 1.2).
Para el "Disminuir", se seleccionan todos los elementos h1, h2 y p en la página, se obtiene su tamaño de fuente actual y se reduce en un 16.67% (/ 1.2).

```
document.addEventListener("DOMContentLoaded", function() {
    const botonAumentar = document.getElementById("btn-aumentar");
    const botonDisminuir = document.getElementById("btn-disminuir");

    botonAumentar.addEventListener("click", function() {
        const elements = document.querySelectorAll("h1, h2, p");

        elements.forEach(element => {
            const currentFontSize = window.getComputedStyle(element).fontSize;
            element.style.fontSize = parseFloat(currentFontSize) * 1.2 + "px";
        });
    });

    botonDisminuir.addEventListener("click", function() {
        const elements = document.querySelectorAll("h1, h2, p");

        elements.forEach(element => {
            const currentFontSize = window.getComputedStyle(element).fontSize;
            element.style.fontSize = parseFloat(currentFontSize) / 1.2 + "px";
        });
    });
});

```


2- Validación formulario
Hemos añadido una funcionalidad de validación al formulario de soporte en la página web.

El archivo JS correspondiente incluye una funcionalidad parecida a la de la modificación del tamaño:
La función se ejecuta cuando el documento HTML ha sido cargado y parseado.
```
document.addEventListener("DOMContentLoaded", function() {

```


```
const form = document.getElementById("support-form");
const mensajeError = document.getElementById("mensaje-error");
const mensajeResaltado = document.getElementById("mensaje-resaltado");
const palabrasProhibidas = ["palabra1", "palabra2", "palabra3"];
```


Se añade EventListener al formulario y se obtiene y comprueba el mensaje del usuario:
```
form.addEventListener("submit", function(event) {
const mensajeInput = document.querySelector("textarea[name='mensaje']");
const textoMensaje = mensajeInput.value;
let tienePalabrasProhibidas = false;
let palabrasEncontradas = [];

```
Recorremos las palabras prohibidas y se comprueba si están presentes en el mensaje del usuario utilizando expresiones regulares.
Si se encuentran, se marcan como encontradas y se añaden a la lista de palabras encontradas.

```
palabrasProhibidas.forEach(palabra => {
    const regex = new RegExp(`\\b(${palabra})\\b`, 'gi');
    if (regex.test(textoMensaje)) {
        tienePalabrasProhibidas = true;
        palabrasEncontradas.push(`<span class="highlight">${palabra}</span>`);
    }
});

```

Por último, mostramos mensajes de error y prevenimos el envío del formulario:
```
if (tienePalabrasProhibidas) {
    event.preventDefault();
    mensajeError.style.display = "block";
    mensajeResaltado.style.display = "block";
    mensajeResaltado.innerHTML = palabrasEncontradas.join(', ');
} else {
    mensajeError.style.display = "none";
    mensajeResaltado.style.display = "none";
}


```


3- Actualizar estado del pedido asíncronamente:
Añadimos interactividad al formulario en la página web, permitiendo actualizar el estado de un pedido sin recargar la página

Esperar a que el DOM esté Cargado:
```
document.addEventListener("DOMContentLoaded", function() {
```
La función se ejecuta cuando el documento HTML ha sido completamente cargado y parseado.

Seleccionar Elementos del DOM:

```
const form = document.getElementById("form-estado");
const btnActualizar = document.getElementById("btn-actualizar");
```
Seleccionamos el formulario y el botón de actualización por sus IDs.
Prevenir el Envío del Formulario por Defecto:

```
form.addEventListener("submit", function(event) {
    event.preventDefault();
});
```
Se previene el comportamiento por defecto del envío del formulario para manejarlo con JavaScript.
Añadir Event Listener al Botón de Actualización:

```
btnActualizar.addEventListener("click", function(event) {
    event.preventDefault();
    const estado = document.getElementById("estado").value;
    const url = form.action;
```
Prevenimos el comportamiento por defecto del botón de actualización.
Obtenemose el valor del nuevo estado del pedido desde un campo de entrada y la URL de acción del formulario.
Enviar la Solicitud Fetch:

```
fetch(url, {
    method: 'POST',
    headers: {
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
        'estado': estado
    })
})
.then(response => response.json())
.then(data => {
```
Envío de solicitud POST a la URL del formulario usando fetch.
Encabezados para el token CSRF y el tipo de contenido.
Envío del nuevo estado del pedido en el cuerpo de la solicitud.
Procesar la Respuesta del Servidor:

```
.then(response => response.json())
.then(data => {
    if (data.success) {
        const estadoSpan = document.getElementById("estado-pedido");
        estadoSpan.textContent = data.estado;
        const pedidoItem = document.querySelector('.pedido-item');
        pedidoItem.className = 'pedido-item pedido-' + estado.replace(" ", "_").toLowerCase();
    } else {
        alert('Error: ' + data.error);
    }
})
.catch(error => console.error('Error:', error));
```
Si la respuesta del servidor indica éxito (data.success), se actualiza el contenido del elemento que muestra el estado del pedido.
Se actualiza también la clase del elemento del pedido para reflejar visualmente el nuevo estado.
Si hay un error, se muestra una alerta con el mensaje de error.
Se maneja cualquier error en la solicitud fetch y se imprime en la consola.




4- Toogle para mostrar y ocultar

Esperar a que el DOM esté Cargado:

```
document.addEventListener("DOMContentLoaded", function() {
```
La función se ejecuta cuando el documento HTML ha sido completamente cargado y parseado.
Seleccionar Elementos del DOM:

```
const toggleButton = document.getElementById("btn-toggle");
const infoBlock = document.getElementById("info");
```
Seleccionamos el botón de alternancia/ toogle y el bloque de información por sus IDs.
Añadir Event Listener al Botón de Alternancia:

```
toggleButton.addEventListener("click", function() {
```
Añadimos un event listener para el evento click del botón de alternancia.
Alternar la Visibilidad del Bloque de Información:

```
if (infoBlock.style.display === "none" || infoBlock.style.display === "") {
    infoBlock.style.display = "block";
    toggleButton.textContent = "Ocultar Información";
} else {
    infoBlock.style.display = "none";
    toggleButton.textContent = "Expandir Información";
}
```
Verificamos si el bloque de información está actualmente oculto (display: none) o sin estilo aplicado (display: "").
Si el bloque está oculto, se cambia su estilo a display: block para mostrarlo y se actualiza el texto del botón a "Ocultar Información".
Si el bloque está visible, se cambia su estilo a display: none para ocultarlo y se actualiza el texto del botón a "Expandir Información".

# Implementaciones no operativas o con errores especificadas si las hubiera.



# Documentacion extra de ayuda.

