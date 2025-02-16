from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()

    def _str_ (self):
        return self.nombre
    
    
    def to_dict(self):
        return {
            # 'ClaveValor': 'Valor'
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.imagen
        }