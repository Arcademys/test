from django.shortcuts import render, redirect
from .models import Autor, Editorial, Libro
from .forms import AutorForm, EditorialForm, LibroForm, BuscarLibroForm

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_autor')
    else:
        form = AutorForm()
    return render(request, 'administracion/crear_autor.html', {'form': form})

def crear_editorial(request):
    # Lógica similar a crear_autor

def crear_libro(request):
    # Lógica similar a crear_autor

def buscar_libro(request):
    if request.method == 'POST':
        form = BuscarLibroForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            libros = Libro.objects.filter(titulo__icontains=titulo)
            return render(request, 'administracion/buscar_libro.html', {'form': form, 'libros': libros})
    else:
        form = BuscarLibroForm()
    return render(request, 'administracion/buscar_libro.html', {'form': form})