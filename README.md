Sistema de Inventario para la Tienda VideoGames

Descripción General

El sistema de inventario desarrollado para la tienda VideoGames es una plataforma web que permite la gestión eficiente de videojuegos y su disponibilidad en el inventario. Proporciona funcionalidades específicas para el control de stock, la categorización de productos por género, y la administración de usuarios según roles, asegurando una experiencia optimizada tanto para los empleados como para los administradores.

Colaboradores
Eliseo Chavez Trujillo
https://github.com/EChavezDevs


Funcionalidades

Gestión de Juegos

Registro de nuevos videojuegos, incluyendo:

Nombre del juego.

Género (con opciones predefinidas como Acción, Aventura, RPG, etc.).

Fecha de publicación.

Empresa desarrolladora.

Cantidad en stock.

Actualización y eliminación de información de juegos.

Gestión de Usuarios

Creación de perfiles con roles específicos:

Administrador: Control total del sistema.

Empleado: Gestión del stock de videojuegos.

Sistema de autenticación con credenciales seguras.

Redirección automática según el tipo de usuario.

Gestión de Stock

Incremento y decremento del stock de videojuegos.

Visualización en tiempo real del inventario disponible.

Restricciones de Seguridad

Impide la eliminación de juegos con stock existente.

Validación de datos antes de realizar cualquier acción crítica.

Interfaz de Usuario

Diseño moderno e intuitivo con Bootstrap.

Navegación sencilla y responsiva, adecuada para diferentes dispositivos.

Requisitos Técnicos

Software

Python: 3.8+

Django: 4.2+

MySQL: 8.0+

XAMPP: Para gestión local de la base de datos.

Bootstrap: 5.0+ para la interfaz de usuario.

Instalación

Clona el repositorio:

git clone https://github.com/EChavezDevs/VideoGames

Instala las dependencias necesarias:

pip install -r requirements.txt

Configura la base de datos en settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'VideoGames',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Ejecuta las migraciones:

python manage.py makemigrations
python manage.py migrate

Inicia el servidor:

python manage.py runserver

Accede a la aplicación en tu navegador:
http://127.0.0.1:8000

Estructura del Proyecto

Gestor de Juegos: Administra la creación, edición y eliminación de videojuegos.

Gestor de Perfiles: Gestiona usuarios y roles.

Gestor de Stock: Permite ajustar la cantidad de juegos disponibles en el inventario.

Base de Datos: MySQL para el almacenamiento de datos.

Interfaz de Usuario: Basada en Bootstrap para un diseño limpio y moderno.

Roles de Usuario

Administrador: Acceso completo al sistema, incluyendo la gestión de juegos y usuarios.

Empleado: Gestión del stock de videojuegos y consulta de inventario.

Seguridad

Encriptación de contraseñas para proteger datos sensibles.

Control de acceso basado en roles.

Validación exhaustiva para evitar inconsistencias en el inventario.
