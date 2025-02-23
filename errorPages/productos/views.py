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
            'id':p.id,
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

from django.shortcuts import get_object_or_404
#funciones para el metodo PUT
def actualizar_producto(request,id_producto):
    if request.method == 'PUT':
        producto = get_object_or_404(Producto, id=id_producto)
        try:
            #la informacion de la modifciacion viene del body del request
            data = json.loads(request.body)
            producto.nombre = data.get('nombre', producto.nombre)
            producto.precio = data.get('precio', producto.precio)
            producto.imagen = data.get('imagen', producto.imagen)
            producto.save()
            return JsonResponse({'mensaje' : 'Producto actualizado correctamente'}, status = 200)
        except Exception as e:
            return JsonResponse({'error':str(e)}, status = 400)
    return JsonResponse({'error':'Metodo no es PUT'}, status = 405)

#Funciones para el Delete
def borrar_producto(request,id_producto):
    if request.method == 'DELETE':
        producto = get_object_or_404(Producto, id=id_producto)
        producto.delete()
        return JsonResponse({'mensaje': 'Producto eliminado correctamente'}, status = 200)
    return JsonResponse({'mensaje':'El metodo no es DELETE'}, status = 405)

#Funcion adicional para un producto en especifico
def obtener_producto(request,id_producto):
    if request.method == 'GET':
        producto = get_object_or_404(Producto, id=id_producto)
        data = {
            "id": producto_id,
            "nombre" : producto.nombre,
            "precio": producto.precio,
            "imagen": producto.imagen
        }
        return JsonResponse(data, status = 200)
    return JsonResponse({'mensaje':'El metodo no es GET'}, status = 405)
    