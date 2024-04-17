
# se registran los modelos de la aplicacion para que sean accesibles desde el panel de administracion de Django
#se puede personalizar como se muestran los modelos en el panel de administracion y que campos son editables

#modelos de la aplicacion (models.py)
#panel de adminitracion (admin.py): interfaz de usuario integrada para administrar los datos de la app


from django.contrib import admin

from appEmpresaDjango.models import Pedido, Productos, Componente

# Register your models here.
admin.site.register(Pedido)
admin.site.register(Productos)
admin.site.register(Componente)