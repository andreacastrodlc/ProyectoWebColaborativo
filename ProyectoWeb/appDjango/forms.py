from django import forms

from appDjango.models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'