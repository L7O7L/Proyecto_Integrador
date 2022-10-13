from enum import unique
from django.db import models

# Create your models here.

class Tipo_user(models.Model):

    tipo = models.CharField(max_length=200)

    class Meta: 

        verbose_name = "Tipo de usuario"
        verbose_name_plural = "Tipos de usuarios"

    def __str__(self):
        return self.tipo

class Usuario(models.Model):

    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres', max_length=200, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=200, blank=False, null=False)
    fecha_nac = models.DateField('Fecha de nacimiento', blank=False, null=False)
    dni = models.CharField('DNI', max_length=8, unique=True, blank=False, null=False)
    correo = models.EmailField('Correo electronico', max_length=200, unique=True ,blank=False, null=False)
    password = models.CharField('Contraseña', max_length=200, blank=False, null=False)
    telefono = models.CharField('Telefono', max_length=9, unique=True, blank=False, null=False)
    tipo = models.ForeignKey(Tipo_user, on_delete = models.CASCADE)

    class Meta: 

        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"            

    def __str__(self):
        return self.apellidos + ", " + self.nombres
    