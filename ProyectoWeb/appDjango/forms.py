from django import forms

from appDjango.models import Producto, Pedido, Componente, Contenidopedido


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['fecha_pedido', 'cif_cliente']  #para que en el formulario solo se pidan esos datos del pedido, ya que el precio total se calcula


class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'


class ContenidoPedidoForm(forms.ModelForm):
    class Meta:
        model = Contenidopedido
        fields = ['referencia_pedido', 'referencia_producto', 'cantidad_producto']
