from django.db import models
# python -m pip install Pillow
#instalar
# Create your models here.
class Juego(models.Model):
    TIPOS_JUEGOS = [
        ('ACCION', 'accion'),
        ('ACCION Y AVENTURA', 'accion y aventura'),
        ('CASUAL', 'casual'),
        ('ESTRATEGIA', 'estrategia'),
        ('SHOOTERS', 'shooters'),
        ('DEPORTES', 'deportes'),
        ('RPG', 'rpg'),
        ('SIMULACION', 'simulacion'),
        ('MMO', 'mmo'),
        ('MMORPG', 'mmorpg'),
    ]
    PG = [
        ('G', 'Todas las edades'),
        ('PG', 'Inadecuado para niños'),
        ('R', 'Diciesiete años en adelante'),
        ('X', 'Mayores de edad')
    ]

    OFERTA = [
        ('0', '0%'),
        ('5', '5%'),
        ('10', '10%'),
        ('15', '15%'),
        ('20', '20%'),
        ('25', '25%'),
        ('30', '30%'),
        ('35', '35%'),
        ('40', '40%'),
        ('45', '45%'),
        ('50', '50%'),
        ('55', '55%'),
        ('60', '60%'),
        ('65', '65%'),
        ('70', '70%'),
        ('75', '75%'),
        ('80', '80%'),
        ('85', '85%'),
        ('90', '90%'),
    ]
    nombre = models.CharField(max_length=255, unique=True)
    stock = models.IntegerField()
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=20, choices=TIPOS_JUEGOS)
    empresa = models.CharField(max_length=255)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    pg = models.CharField(max_length=18, choices=PG)
    horas_juego = models.IntegerField()
    oferta = models.CharField(max_length=20, choices=OFERTA)
    imagen_url = models.URLField(max_length=500, blank=True, null=True)
