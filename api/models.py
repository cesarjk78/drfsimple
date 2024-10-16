from django.db import models

# Create your models here.


class Programmer(models.Model):
    nombre = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    apodo = models.CharField(max_length=60, default="Sin Apodo")
    descripcion = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre