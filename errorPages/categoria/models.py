from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.URLField()
    
    def _str_(self):
        return self.nombre
    
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'imagen': self.imagen
        }