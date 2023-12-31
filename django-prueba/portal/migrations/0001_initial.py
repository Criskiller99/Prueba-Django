# Generated by Django 4.2.7 on 2023-11-14 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('nit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ofertas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('salario', models.IntegerField()),
                ('habilidades', models.TextField()),
                ('fecha_creacion', models.DateTimeField()),
                ('fecha_actualizacion', models.DateTimeField()),
                ('empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=200)),
                ('segundo_nombre', models.CharField(max_length=200)),
                ('primer_apellido', models.CharField(max_length=200)),
                ('segundo_apellido', models.CharField(max_length=200)),
                ('descripcion_perfil', models.TextField()),
                ('numero_identificacion', models.IntegerField()),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Postulacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ofertas_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.ofertas')),
                ('Usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.usuario')),
            ],
        ),
    ]
