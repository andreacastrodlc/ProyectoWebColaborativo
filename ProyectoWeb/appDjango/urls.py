from django.urls import path
from .views import ProductoListView, ProductoDetailView, ProductoCreateView

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='index_productos'),
    path('productos/<int:pk>', ProductoDetailView.as_view(), name='productos_show'),
    path('productos/create', ProductoCreateView.as_view(), name='producto_create')
]