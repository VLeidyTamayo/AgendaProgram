from django.db import models

# Create your models here.

class contactos(models.Model):
    avatar = models.ImageField(upload_to='contactos',null=True,blank=True)
    nombre = models.CharField(max_length=100)
    email= models.EmailField(max_length=50) #Validaciones del campo
    fecha = models.DateField(null=True, blank=True) #No obligatorio el campo y en blanco en formulario de Djgango
    telefono = models.CharField(max_length=15, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True) #Para auditoria gestión automaticamente fecha y hora creación
    
    "Mostrar en el panel de administración los nombres de los contactos"
    def __str__(self) -> str:
        return self.nombre
    
    