from django.urls import path

from .views import (ProductoListView, ProductoDetailView, ProductoCreateView, PedidoListView, PedidoCreateView,
                    PedidoDetailView, ComponenteListView, ComponenteDetailView, ComponenteCreateView,
                    asignar_componentes_producto, ProductoDeleteView, ProductoUpdateView, asignar_productos_pedido,
                    ProductoUpdateView, ProductoDeleteView, ClienteListView, ClienteDetailView, ClienteCreateView,
                    ClienteDeleteView, ClienteUpdateView)

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='index_productos'),
    path('productos/<int:pk>', ProductoDetailView.as_view(), name='productos_show'),
    path('productos/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_delete'),
    path('productos/modificar/<int:pk>', ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/create', ProductoCreateView.as_view(), name='producto_create'),
    path('clientes/', ClienteListView.as_view(), name='index_clientes'),
    path('clientes/<int:pk>', ClienteDetailView.as_view(), name='clientes_show'),
    path('clientes/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
    path('clientes/modificar/<int:pk>', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/create', ClienteCreateView.as_view(), name='cliente_create'),
    path('pedidos/', PedidoListView.as_view(), name='index_pedidos'),
    path('pedidos/<int:pk>', PedidoDetailView.as_view(), name='pedidos_show'),
    path('pedidos/create', PedidoCreateView.as_view(), name='pedido_create'),
    path('componentes/', ComponenteListView.as_view(), name='index_componentes'),
    path('componentes/<int:pk>', ComponenteDetailView.as_view(), name='componente_show'),
    path('componentes/create', ComponenteCreateView.as_view(), name='componente_create'),
    path('productos/<int:pk>/asignar_componentes/', asignar_componentes_producto, name='asignar_componentes_producto'),
    path('asignar_productos_pedido/<int:pk_pedido>', asignar_productos_pedido, name='asignar_productos_pedido')
]