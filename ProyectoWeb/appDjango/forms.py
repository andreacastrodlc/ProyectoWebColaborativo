from django import forms

from appDjango.models import Producto, Pedido, Componente


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['fecha_pedido', 'cif_cliente'] #para que en un primer formulario solo se pidan esos datos del pedido


class PrecioPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['precio_total'] #para que en un posterior formulario se pida el precio total del pedido


class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'
