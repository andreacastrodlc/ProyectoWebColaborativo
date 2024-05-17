from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from appDjango.models import Producto, Pedido, Componente, Contenidopedido, Cliente


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['fecha_pedido', 'cif_cliente']
        # para que en el formulario solo se pidan esos datos del pedido, ya que el precio total se calcula


class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'


class ContenidoPedidoForm(forms.ModelForm):
    class Meta:
        model = Contenidopedido
        fields = ['referencia_pedido', 'referencia_producto', 'cantidad_producto']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
