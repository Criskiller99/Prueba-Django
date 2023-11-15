# Generated by Django 4.2.7 on 2023-11-15 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='usuario_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ofertas',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ofertas',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
