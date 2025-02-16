from django.shortcuts import render, redirect
from .models import Producto
from django.http import JsonResponse

from .forms import ProductoForm

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
    else:
        form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})


def lista_productos(request):
    productos = Producto.objects.all()
    
    data = [
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]
    
    return JsonResponse(data, safe=False)

def ver_productos(request):
    return render(request, 'ver.html')
