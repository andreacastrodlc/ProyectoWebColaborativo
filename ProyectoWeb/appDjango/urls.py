from django.urls import path
from .views import (ProductoListView, ProductoDetailView, ProductoCreateView, PedidoListView, PedidoCreateView,
                    PedidoDetailView)

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='index_productos'),
    path('productos/<int:pk>', ProductoDetailView.as_view(), name='productos_show'),
    path('productos/create', ProductoCreateView.as_view(), name='producto_create'),
    path('pedidos/', PedidoListView.as_view(), name='index_pedidos'),
    path('pedidos/<int:pk>', PedidoDetailView.as_view(), name='pedidos_show'),
    path('pedidos/create', PedidoCreateView.as_view(), name='pedido_create')
]