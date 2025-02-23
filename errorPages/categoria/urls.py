from django.urls import path
from .views import *

urlpatterns = [

    path('registrar/', registrar_categoria, name='registrar_categoria'),
    path('json/', json_categoria, name='json_categoria'),
    path('api/get', lista_categoria, name='lista_categoria'),
    path('api/post/', registrar_categorias, name='post'),
    path('api/delete/<str:id_categoria>/',borrar_categoria, name='delete')
    
]