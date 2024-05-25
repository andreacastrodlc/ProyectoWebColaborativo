from django.db import models

# Create your models here.


class Cliente(models.Model):
    cif_cliente = models.CharField(max_length=100, primary_key=True)
    nombre_empresa_cliente = models.CharField(max_length=255)
    direccion_cliente = models.CharField(max_length=255)
    telefono_cliente = models.IntegerField()
    email_cliente = models.EmailField()

    def __str__(self):
        return (f"CIF: {self.cif_cliente}, Empresa: {self.nombre_empresa_cliente}, Dirección: {self.direccion_cliente},"
                f" Teléfono: {self.telefono_cliente}, Email: {self.email_cliente}")

    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"
        ordering = ["cif_cliente"]


class Pedido(models.Model):
    referencia_pedido = models.AutoField(primary_key=True)
    fecha_pedido = models.DateField()
    cif_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    # default para que no haya errores al crear un nuevo producto sin introducir el precio total
    ESTADO_CHOICES = [
        ("Pendiente", "Pendiente"),
        ("En proceso", "En proceso"),
        ("Enviado", "Enviado"),
        ("Completado", "Completado")
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')

    def __str__(self):
        return (f"Código de referencia: {self.referencia_pedido}, Fecha de pedido: {self.fecha_pedido}, "
                f"{self.cif_cliente}, Precio total: {self.precio_total}, Estado: {self.estado}")

    class Meta:
        verbose_name_plural = "Pedidos"
        verbose_name = "Pedido"
        ordering = ["fecha_pedido"]


class Producto(models.Model):
    referencia_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=255)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion_producto = models.TextField()
    categoria_producto = models.CharField(max_length=100)

    def __str__(self):
        return (f'Referencia: {self.referencia_producto},Nombre: {self.nombre_producto}, '
                f'Precio: {self.precio_producto}, Descripcion: {self.descripcion_producto}, '
                f'Categoria: {self.categoria_producto}')

    class Meta:
        verbose_name_plural = "Productos"
        verbose_name = "Producto"
        ordering = ["nombre_producto"]


class Contenidopedido(models.Model):
    referencia_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    referencia_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto = models.IntegerField()

    def __str__(self):
        return (f'{self.referencia_pedido}, {self.referencia_producto}, '
                f'Cantidad producto: {self.cantidad_producto}')

    class Meta:
        ordering = ["referencia_pedido"]


class Componente(models.Model):
    referencia_componente = models.AutoField(primary_key=True)
    modelo_componente = models.CharField(max_length=255)
    marca_componente = models.CharField(max_length=100)

    def __str__(self):
        return (f"Codigo de referencia: {self.referencia_componente}, Modelo: {self.modelo_componente}, "
                f"Marca: {self.marca_componente}")

    class Meta:
        verbose_name_plural = "Componentes"
        verbose_name = "Componente"
        ordering = ["referencia_componente"]


class ComponenteProducto(models.Model):
    referencia_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    referencia_componente = models.ForeignKey(Componente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.referencia_producto}, {self.referencia_componente}"

    class Meta:
        ordering = ["referencia_producto"]
