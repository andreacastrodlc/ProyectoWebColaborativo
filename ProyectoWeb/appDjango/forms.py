from django import forms
from django.contrib.auth.forms import UserCreationForm  # import de formulario de creacion de usuario propio de Django
from django.contrib.auth.models import User  # import del modelo User propio de Django

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


# formulario de registro que hereda de UserCreationForm (proporcionado por Django para manejar la creacion de usuarios
# con contrasenas)
class RegistroForm(UserCreationForm):
    # campo adicional de email requerido obligatoriamente
    email = forms.EmailField(required=True)

    class Meta:
        # se utiliza el modelo user proporcionado por Django
        model = User
        # campos que se utilizan en el formulario
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        # se guardan los datos del formulario por defecto (sin email porque es un campo adicional creado)
        user = super().save(commit=False)
        # se anade el campo de email del formulario
        user.email = self.cleaned_data['email']
        # se guarda el usuario en la base de datos
        if commit:
            user.save()
        return user
