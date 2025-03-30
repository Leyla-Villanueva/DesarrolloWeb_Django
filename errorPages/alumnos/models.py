from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Alumno(models.Model):
    '''
    Nombre
    Apellido
    Edad
    Matricula (único)
    Correo (único)
    '''
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    matricula = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True, max_length=100)
    
    def __str__ (self):
        return self.nombre
    
    # Necesito una funcion que devuelva el objeto en fomra de Dict 
    
    def to_dict(self):
        return {
            # 'ClaveValor': 'Valor'
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'matricula': self.matricula,
            'email': self.email
        }