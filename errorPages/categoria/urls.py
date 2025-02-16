from django.urls import path
from .views import *

urlpatterns = [
    path('api/get', lista_categoria, name='lista_categoria'),
    path('json/', json_categoria, name='json_categoria'),
    path('registrar/', registrar_categoria, name='registrar_categoria'),
]