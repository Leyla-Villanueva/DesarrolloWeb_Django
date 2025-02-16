from django.shortcuts import render, redirect
from .models import Categoria
from django.http import JsonResponse

from .forms import CategoriaForm

def registrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('json_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'registrar.html', {'form': form})


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