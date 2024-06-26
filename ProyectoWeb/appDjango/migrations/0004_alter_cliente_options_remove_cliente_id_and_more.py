# Generated by Django 4.2.11 on 2024-04-28 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0003_cliente_remove_pedido_cif_cliente_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['cif_cliente'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.RemoveField(
            model_name='componente',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cantidad_producto',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='producto_solicitado',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='id',
        ),
        migrations.AddField(
            model_name='pedido',
            name='cif_cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appDjango.cliente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cif_cliente',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='componente',
            name='referencia_componente',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='referencia_pedido',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='referencia_producto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Contenidopedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto', models.IntegerField()),
                ('referencia_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDjango.pedido')),
                ('referencia_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDjango.producto')),
            ],
            options={
                'ordering': ['referencia_pedido'],
            },
        ),
        migrations.CreateModel(
            name='ComponenteProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia_componente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDjango.componente')),
                ('referencia_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDjango.producto')),
            ],
            options={
                'ordering': ['referencia_producto'],
            },
        ),
    ]
