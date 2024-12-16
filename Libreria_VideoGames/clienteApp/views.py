from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioForm, UsuarioUpdateForm, UserUpdateForm
from django.contrib.auth.models import Group, User
from juegosApp.models import Juego
from clienteApp.models import Usuario
from django.contrib.auth.decorators import login_required
#Group.objects.get_or_create(name='Cliente')
# Create your views here.

def crear_cuenta(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            django_user = User.objects.create_user(username=username, password=password)
            usuario = form.save(commit=False)
            usuario.django_user = django_user
            usuario.save()
            grupo_cliente = Group.objects.get(name='Cliente')
            django_user.groups.add(grupo_cliente)

            messages.success(request, 'Cuenta creada exitosamente.')
            return redirect('login')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = UsuarioForm()

    return render(request, 'Usuario/crear_cuenta.html', {'form': form})


@login_required
def actualizar_datos(request):
    try:
        usuario = request.user.usuario
    except Usuario.DoesNotExist:
        messages.error(request, 'No se encontró el perfil de usuario.')
        return redirect('cliente')
    if request.method == 'POST':
        usuario_form = UsuarioUpdateForm(request.POST, instance=usuario)
        user_form = UserUpdateForm(request.POST, instance=request.user) 
        if usuario_form.is_valid() and user_form.is_valid():
            usuario_form.save()
            user_form.save()
            return redirect('cliente')
    else:
        usuario_form = UsuarioUpdateForm(instance=usuario)
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'usuario_form': usuario_form,
        'user_form': user_form
    }
    return render(request, 'Usuario/actualizar_datos.html', context)

#CARRITO

def agregar_al_carrito(request, nombre_juego):
    carrito = request.session.get('carrito', {})

    # Si el juego ya está en el carrito, aumentamos la cantidad
    if nombre_juego in carrito:
        carrito[nombre_juego] += 1
    else:
        carrito[nombre_juego] = 1

    request.session['carrito'] = carrito

    return redirect('cliente')

def carrito_view(request):
    carrito = request.session.get('carrito', {})

    juegos = []
    for nombre_juego, cantidad in carrito.items():
        try:
            # Usamos el nombre del juego para obtener el objeto Juego
            juego = Juego.objects.get(nombre=nombre_juego)
            juegos.append({'juego': juego, 'cantidad': cantidad})
        except Juego.DoesNotExist:
            continue 

    return render(request, 'Usuario/carrito.html', {'juegos': juegos})

def quitar_del_carrito(request, juego_nombre):
    carrito = request.session.get('carrito', {})

    if juego_nombre in carrito:
        del carrito[juego_nombre]  # Eliminamos el juego por su nombre

    request.session['carrito'] = carrito

    return redirect('carrito')

def realizar_pedido(request):
    carrito = request.session.get('carrito', {})

    if not carrito:
        return redirect('carrito')  # Si el carrito está vacío, volvemos al carrito

    for nombre_juego, cantidad in carrito.items():
        try:
            # Usamos el nombre del juego para obtener el objeto Juego
            juego = Juego.objects.get(nombre=nombre_juego)

            # Verificamos si hay suficiente stock
            if juego.stock >= cantidad:
                juego.stock -= cantidad
                juego.save()
            else:
                return redirect('stock_insuficiente')  # Si no hay suficiente stock

        except Juego.DoesNotExist:
            continue  # Si el juego no existe, ignoramos el error

    # Limpiamos el carrito una vez procesado el pedido
    request.session['carrito'] = {}

    return render(request, 'Usuario/pedido_realizado.html')