from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import JuegoForm
from .models import Juego
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    juegos = Juego.objects.all()
    return render(request, 'index.html', {'juegos': juegos})


@login_required
def usuario_comun_view(request):
    juegos = Juego.objects.all()
    return render(request, 'cliente.html', {'juegos': juegos})
 

@login_required
def admi_view(request):
    return render(request, 'admi.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if user.groups.filter(name="Cliente").exists():
                return redirect('cliente')
            elif user.groups.filter(name="Administradores").exists():
                return redirect('admi') 
        
        else:
            messages.error(request, "Formulario inválido.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    auth_logout(request) 
    return redirect('login')

def listaJuego(request):
    juegos = Juego.objects.all()
    data = {'juegos': juegos}
    return render(request, 'CRUD/juegos.html', data)

def agregaJuego(request):
    form = JuegoForm()
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Se ha agregado correctamente el juego.")  
            return redirect('listaJuego')
    data = {'form': form}
    return render(request, 'CRUD/agregaJuegos.html', data)

def eliminaJuego(request, id):
    juego = get_object_or_404(Juego, id=id) 
    juego.delete() 
    messages.success(request, "Se ha eliminado correctamente el juego.")
    return redirect('listaJuego') 

def actualizaJuego(request, id):
    juego = get_object_or_404(Juego, id=id)
    form = JuegoForm(instance=juego)
    if request.method == 'POST':
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save() 
            messages.success(request, "Se ha actualizado correctamente el juego.")  
            return redirect('listaJuego')
    data = {'form': form}
    return render(request, 'CRUD/agregaJuegos.html', data)


#APIS
from rest_framework import generics
from .serializers import JuegoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

class CrearJuego(generics.CreateAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer
    permission_classes = [IsAuthenticated]

class ListaJuegoAPIView(generics.ListCreateAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer
    permission_classes = [IsAuthenticated]

class JuegoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs['pk']
        try:
            return Juego.objects.get(pk=pk)
        except Juego.DoesNotExist:
            raise NotFound(f"Juego con id {pk} no encontrado.")

