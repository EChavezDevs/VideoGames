from django.contrib import admin
from juegosApp.models import Juego
# Register your models here.
class InformacionJuego(admin.ModelAdmin):
    list_display = ['nombre', 'stock', 'fecha_publicacion', 'genero', 'empresa', 'precio', 'descripcion', 'pg', 'horas_juego', 'oferta', 'imagen_url'] 
admin.site.register(Juego, InformacionJuego)
