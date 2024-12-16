from rest_framework import serializers
from .models import Juego

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['id', 'nombre', 'stock', 'fecha_publicacion', 'genero', 'empresa', 'precio', 'descripcion', 'pg', 'horas_juego', 'oferta', 'imagen_url']

