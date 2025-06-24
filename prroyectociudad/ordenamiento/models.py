from django.db import models

# Create your models here.

class Parroquia (models.Model):
    UBI_CHOICES = [
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste')
    ]
    TIPO_CHOICES = [
        ('urbana', 'Urbana'),
        ('rural', 'Rural')
    ] 
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=10, choices=UBI_CHOICES)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre 

    


class Barrio (models.Model):
    PARQUES_CHOICES = [
        (1, '1 parque'),
        (2, '2 parques'),
        (3, '3 parques'),
        (4, '4 parques'),
        (5, '5 parques'),
        (6, '6 parques'),
    ]
    nombre = models.CharField(max_length=100)
    numero_viviendas = models.PositiveIntegerField()
    numero_parques = models.PositiveSmallIntegerField(choices=PARQUES_CHOICES)
    nume_edificios_residenciales = models.PositiveIntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name='barrios')
    
    def __str__(self):
        return self.nombre
    
