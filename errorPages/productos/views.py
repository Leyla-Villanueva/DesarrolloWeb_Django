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

import json

def registrar_producto(request):
    # checar si nuestra request es de tipo post
    if request.method == 'POST':
        try:
            data = json.loads(request.body) # texto json
            producto = Producto.objects.create(
                nombre=data['nombre'],
                precio=data['precio'],
                imagen=data['imagen']
            ) #create directamente mete el objeto en la BD
            return JsonResponse(
                {
                    'mensaje':'registro exitoso',
                    'id':producto.id
                },status=201
            )
        except Exception as e:
            print(str(e))
            return JsonResponse(
                {'error':str(e)}, status = 400
            )
    #si no es post el request
    return JsonResponse(
        {'error':'El metodo no esta soportado'}, status=405
    )
