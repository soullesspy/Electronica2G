from django.db import models

# Create your models here.

class Cliente (models.Model):
    codigo = models.CharField(max_length=200, unique=True, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    cedula_ruc = models.CharField(max_length=10, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    codigo = models.CharField(max_length=200, unique=True, null=True, blank=True)
    nombre_producto = models.CharField(max_length=255, unique=True, null=True, blank=True)
    descripcion = models.CharField(max_length=255, unique=True, null=False)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    costo = models.IntegerField(null=False)
    cantidad = models.IntegerField(null=False)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'Productos'
        order_with_respect_to = 'nombre_producto'
    
    def __str__(self):
        return self.nombre_producto


