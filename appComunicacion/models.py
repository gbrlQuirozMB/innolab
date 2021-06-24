from django.db import models


class DatosCorreo(models.Model):
    creado_en = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    servicioDeseado = models.CharField(max_length=200, db_column='servicio_deseado')

    class Meta:
        db_table = 'datos_correo'
        ordering = ['-id']
