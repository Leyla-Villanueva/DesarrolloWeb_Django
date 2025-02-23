import json
from django.shortcuts import get_object_or_404, render, redirect
from .models import Categoria

from django.http import JsonResponse

from .forms import CategoriaForm




def lista_categoria(request):
    categorias = Categoria.objects.all()

    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categorias
    ]
    
    return JsonResponse(data, safe=False)

def json_categoria(request):
    return render(request, 'json.html')


def registrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('json_categoria')
    else:
        form = CategoriaForm()

    return render(request, 'registrar.html', {'form': form})


def registrar_categorias(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            categoria = categoria.objects.create(
                nombre=data['nombre'], imagen=data['imagen']
            )
            return JsonResponse(
                {
                    'mensaje':'registro exitoso',
                    'id':categoria.id
                },status=201
            )
        except Exception as e:
            return JsonResponse(
                {'error':str(e)}, status = 400)
    return JsonResponse(
        {'error':'El metodo no esta soportado'}, status=405
    )

def borrar_categoria(request,id_categoria):
    if request.method == 'DELETE':
        categoria = get_object_or_404(categoria, id=id_categoria)
        categoria.delete()
        return JsonResponse({'mensaje': 'categoria eliminado correctamente'}, status = 200)
    return JsonResponse({'mensaje':'El metodo no es DELETE'}, status = 405)
