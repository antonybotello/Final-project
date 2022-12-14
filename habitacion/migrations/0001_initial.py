# Generated by Django 4.1.1 on 2022-11-04 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoHabitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipoHabitacion', models.CharField(choices=[('Sencilla ', 'Sencilla'), ('Doble', 'Doble'), ('Campestre', 'Campestre')], default='Sencilla ', max_length=10, verbose_name='Nombre Tipo de Habitacion')),
                ('complementosTipoHabitacion', models.CharField(max_length=50, verbose_name='Complementos Tipo Habitacion')),
                ('valorTipoHabitacion', models.IntegerField(verbose_name='Valor Tipo Habitacion')),
                ('descripcionTipoHabitacion', models.CharField(max_length=200, verbose_name='Descripcion Tipo Habitacion')),
                ('capacidad', models.CharField(max_length=45, verbose_name='Capacidad')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroHabitacion', models.CharField(max_length=4, verbose_name='Numero de Habitacion')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('disponibilidad', models.CharField(choices=[('Disponible', 'Disponible'), ('Ocupada', 'Ocupada')], default='Disponible', max_length=10, verbose_name='Disponibilidad')),
                ('sede', models.CharField(choices=[('estacion', 'La Estación'), ('bosque', 'El Bosque')], default='estacion', max_length=8, verbose_name='Sede')),
                ('tipoHabitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitacion.tipohabitacion', verbose_name='Tipo Habitacion')),
            ],
        ),
    ]
