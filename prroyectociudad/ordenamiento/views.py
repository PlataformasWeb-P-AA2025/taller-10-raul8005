from django.shortcuts import render, redirect
from .models import *
from .forms import ParroquiaForm, BarrioForm, forms

# Create your views here.

def listar_parroquia_barrio(request):
    parroquias = Parroquia.objects.prefetch_related('barrios').all()
    return render(request, 'ordenamiento/listar_parroquia_barrio.html', {'parroquias': parroquias})


def listar_barrios(request):
    barrios = Barrio.objects.select_related('parroquia').all()
    return render(request, 'ordenamiento/listar_barrios.html', {'barrios': barrios})

# Vistas para los formularios

def crear_parroquia(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Asegúrate que exista la URL con name='inicio'
    else:
        form = ParroquiaForm()
    return render(request, 'ordenamiento/crear_parroquia.html', {'form': form})


def crear_barrio(request):
    form = BarrioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_barrios')
    return render(request, 'ordenamiento/crear_barrio.html', {'form': form})
