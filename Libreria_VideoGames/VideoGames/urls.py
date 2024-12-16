"""
URL configuration for VideoGames project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from juegosApp import views as juegos
from clienteApp import views as clientes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', juegos.index, name='index'),

    path('crear-cuenta/', clientes.crear_cuenta, name='crear_cuenta'),
    

    path('login/', juegos.login_view, name='login'),
    path('logout/', juegos.logout_view, name='logout'),
 
    path('admi/', juegos.admi_view, name='admi'),  # Vista admin
    path('cliente/', juegos.usuario_comun_view, name='cliente'),  # Vista usuarios
    

    path('admi/CRUD/juegos/', juegos.listaJuego, name='listaJuego'),
    path('admi/CRUD/agregaJuegos/', juegos.agregaJuego, name='agregaJuego'),
    path('admi/CRUD/eliminaJuegos/<int:id>/', juegos.eliminaJuego, name='eliminaJuego'),
    path('admi/actualizaJuegos/<int:id>/', juegos.actualizaJuego, name='actualizaJuego'),

    #Cliente
    path('actualizar_datos/', clientes.actualizar_datos, name='actualizar_datos'),
    path('carrito/', clientes.carrito_view, name='carrito'),
    path('agregar_al_carrito/<str:nombre_juego>/', clientes.agregar_al_carrito, name='agregar_al_carrito'),
    path('quitar-del-carrito/<str:juego_nombre>/', clientes.quitar_del_carrito, name='quitar_del_carrito'),
    path('realizar_pedido/', clientes.realizar_pedido, name='realizar_pedido'),

    #APIS
    path('juegos/', juegos.ListaJuegoAPIView.as_view(), name='lista_juegos'),
    path('juegos/crear/', juegos.CrearJuego.as_view(), name='agregar_juego'),
    path('juegos/<int:pk>/', juegos.JuegoDetalle.as_view(), name='detalle_juego'),

]