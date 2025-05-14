from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=45)
    
    def __str__(self):
        return self.descripcion