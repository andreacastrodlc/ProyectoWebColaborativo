from django import forms

from appDjango.models import Producto, Pedido, Componente


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'


class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'