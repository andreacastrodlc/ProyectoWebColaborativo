from django.urls import path
from .views import (ProductoListView, ProductoDetailView, ProductoCreateView, PedidoListView, PedidoCreateView,
                    PedidoDetailView, ComponenteListView, ComponenteDetailView, ComponenteCreateView, asignar_componentes_producto)

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='index_productos'),
    path('productos/<int:pk>', ProductoDetailView.as_view(), name='productos_show'),
    path('productos/create', ProductoCreateView.as_view(), name='producto_create'),
    path('pedidos/', PedidoListView.as_view(), name='index_pedidos'),
    path('pedidos/<int:pk>', PedidoDetailView.as_view(), name='pedidos_show'),
    path('pedidos/create', PedidoCreateView.as_view(), name='pedido_create'),
    path('componentes/', ComponenteListView.as_view(), name='index_componentes'),
    path('componentes/<int:pk>', ComponenteDetailView.as_view(), name='componente_show'),
    path('componentes/create', ComponenteCreateView.as_view(), name='componente_create'),
    path('productos/<int:pk>/asignar_componentes/', asignar_componentes_producto, name='asignar_componentes_producto')
]