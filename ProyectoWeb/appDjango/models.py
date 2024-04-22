from django.db import models

# Create your models here.
class Producto(models.Model):
    referencia_producto = models.CharField(max_length=100, unique=True)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_producto = models.CharField(max_length=255)
    descripcion_producto = models.TextField()
    categoria_producto = models.CharField(max_length=100)

    def __str__(self):
        return (f" Referencia: {self.referencia_producto},Nombre: {self.nombre_producto}, "
                f"Precio: {self.precio_producto}")

    class Meta:
        verbose_name_plural = "Productos"
        verbose_name = "Producto"
        ordering = ["nombre_producto"]


class Pedido(models.Model):
    referencia_pedido = models.CharField(max_length=100, unique=True)
    fecha_pedido = models.DateField()
    producto_solicitado = models.ManyToManyField(Producto)
    cantidad_producto = models.IntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2) #quitar y anadir mediante logica de negocio (precio*cantidad)
    def __str__(self):
        return (f"Código de referencia: {self.referencia_pedido},Producto solicitado: {self.producto_solicitado}, "
                f"Cantidad: {self.cantidad_producto}, Precio total: {self.precio_total}")
    class Meta:
        verbose_name_plural = "Pedidos"
        verbose_name = "Pedido"
        ordering = ["fecha_pedido"]


class Componente(models.Model):
    referencia_componente = models.CharField(max_length=100)
    modelo_componente = models.CharField(max_length=255)
    marca_componente = models.CharField(max_length=100)
    def __str__(self):
        return (f" Codigo de referencia: {self.referencia_componente}, Modelo: {self.modelo_componente}, Marca: {self.marca_componente}")

    class Meta:
        verbose_name_plural = "Componentes"
        verbose_name = "Componente"
        ordering = ["referencia_componente"]


class Cliente(models.Model):
    cif_cliente = models.CharField(max_length=100)
    nombre_empresa_cliente = models.CharField(max_length=255)
    direccion_cliente = models.CharField(max_length=255)
    telefono_cliente = models.IntegerField()
    email_cliente = models.EmailField()
    def __str__(self):
        return (f" CIF: {self.cif_cliente}, Empresa: {self.nombre_empresa_cliente}, Direccion: {self.direccion_cliente},"
                f" Telefono: {self.telefono_cliente}, Email: {self.email_cliente}")
    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"
        ordering = ["cif_cliente"]