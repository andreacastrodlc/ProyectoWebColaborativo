from django.urls import path
from . import views

from .views import ProductoListView, ProductoDetailView, ProductoCreateView, ProductoDeleteView

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='index_productos'),
    path('productos/<int:pk>', ProductoDetailView.as_view(), name='productos_show'),
    path('productos/create', ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:producto>', views.ProductoDeleteView.as_view(), name='producto_delete'),
    path('productos/<int:producto>', views.ProductoUpdateView.as_view(), name='producto_update')

]
