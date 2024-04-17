from django.db import models

# Create your models here.
class Pedido(models.Model):
    codigo_referencia = models.CharField(max_length=100, unique=True)
    fecha = models.DateField()
    cif_cliente = models.CharField(max_length=100)
    nombre_empresa_cliente = models.CharField(max_length=255)
    direccion_cliente = models.CharField(max_length=255)
    datos_contacto_cliente = models.CharField(max_length=255)
    producto_solicitado = models.ManyToManyField(Producto)
    cantidad = models.IntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return (f"Código de referencia: {self.codigo_referencia},Producto solicitado: {self.producto_solicitado}, "
                f"Cantidad: {self.cantidad}, Precio total: {self.precio_total}")
    class Meta:
        verbose_name_plural = "Pedidos"
        verbose_name = "Pedido"
        ordering = ["fecha"]



class Producto(models.Model):
    referencia = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return (f" Referencia: {self.referencia},Nombre: {self.nombre}, "
                f"Precio: {self.precio}")

    class Meta:
        verbose_name_plural = "Productos"
        verbose_name = "Producto"
        ordering = ["nombre"]



class Componente(models.Model):
    codigo_referencia = models.CharField(max_length=100)
    nombre_modelo = models.CharField(max_length=255)
    marca = models.CharField(max_length=100)
    def __str__(self):
        return (f" Codigo de referencia: {self.codigo_referencia}, Modelo: {self.nombre_modelo}, Marca: {self.marca}")

    class Meta:
        verbose_name_plural = "Componentes"
        verbose_name = "Componente"
        ordering = ["codigo_referencia"]