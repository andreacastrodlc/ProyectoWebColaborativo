from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia_componente', models.CharField(max_length=100)),
                ('modelo_componente', models.CharField(max_length=255)),
                ('marca_componente', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Componente',
                'verbose_name_plural': 'Componentes',
                'ordering': ['referencia_componente'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia_producto', models.CharField(max_length=100, unique=True)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nombre_producto', models.CharField(max_length=255)),
                ('descripcion_producto', models.TextField()),
                ('categoria_producto', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nombre_producto'],
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia_pedido', models.CharField(max_length=100, unique=True)),
                ('fecha_pedido', models.DateField()),
                ('cif_cliente', models.CharField(max_length=100)),
                ('nombre_empresa_cliente', models.CharField(max_length=255)),
                ('direccion_cliente', models.CharField(max_length=255)),
                ('datos_contacto_cliente', models.CharField(max_length=255)),
                ('cantidad_producto', models.IntegerField()),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto_solicitado', models.ManyToManyField(to='appDjango.producto')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['fecha_pedido'],
            },
        ),
    ]
