from django.db import models 
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    primer_nombre = models.CharField(max_length=200)
    segundo_nombre = models.CharField(max_length=200)
    primer_apellido = models.CharField(max_length=200)
    segundo_apellido = models.CharField(max_length=200)
    descripcion_perfil = models.TextField()
    numero_identificacion = models.IntegerField()
    telefono = models.IntegerField()
    usuario_id = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
       return self.primer_nombre + " - " +  self.primer_apellido

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    nit = models.IntegerField()
    
    def __str__(self):
       return self.nombre + " - " +  self.nit

class Ofertas(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    salario = models.IntegerField()
    habilidades = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.titulo 

class Postulacion(models.Model):
    Usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Ofertas_id = models.ForeignKey(Ofertas, on_delete=models.CASCADE)
    
    def __str__(self):
       return self



