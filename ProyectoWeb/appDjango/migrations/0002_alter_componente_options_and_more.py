# Generated by Django 4.2.11 on 2024-04-21 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appDjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componente',
            options={'ordering': ['referencia_componente'], 'verbose_name': 'Componente', 'verbose_name_plural': 'Componentes'},
        ),
        migrations.RenameField(
            model_name='componente',
            old_name='referencia_componente',
            new_name='referencia_componente',
        ),
    ]
