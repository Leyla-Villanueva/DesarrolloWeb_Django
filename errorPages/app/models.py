from django.db import models

"""
class Mascotas(models.Model):
    nombre = models.CharField(max_length=60, blank=True, null=True)

class Usuarios(models.Model):
    nombres = models.CharField(max_length=60, blank=True, null=True)
    apellidos = models.CharField(max_length=60, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
"""

class ErrorLog(models.Model):
    codigo = models.CharField(max_length=10)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} - {self.mensaje}"