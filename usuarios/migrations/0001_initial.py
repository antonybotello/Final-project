# Generated by Django 4.1.1 on 2022-10-26 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuarioTipo', models.CharField(choices=[('Administrador', 'Administrador'), ('Recepción', 'Recepción')], default='Recepción', max_length=14, verbose_name='Usuario Tipo')),
                ('contraseña', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=45, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=45, verbose_name='Apellidos')),
                ('tipoDocumento', models.CharField(choices=[('C.C', 'Cédula de Ciudadanía'), ('C.E', 'Cédula de Extrangeriía'), ('P.P', 'Pasaporte'), ('T.I', 'Tarjeta de Identidad'), ('Otro', 'Otro Tipo de Documento')], default='C.C', max_length=5, verbose_name='Tipo de Documento')),
                ('numeroDocumento', models.CharField(max_length=45, verbose_name='Número de Documento')),
                ('telefono', models.CharField(blank=True, max_length=15, verbose_name='Teléfono')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('tipoUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.tipo_usuario', verbose_name='Tipo Usuario')),
            ],
        ),
    ]