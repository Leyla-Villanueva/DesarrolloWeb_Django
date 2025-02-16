from django.contrib import admin
from django.urls import path

from app.views import *
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('error/', generar_error, name='error'),
    path('onepage/', onepage, name='onepage'),
    path('prueba/', prueba_front, name='prueba'),
    path('buscador/', search_view, name='buscador'),
    path('error_logs/', error_logs, name='error_logs'),
    path('api/error_logs/', get_error_logs, name='get_error_logs'),
    path('users/', include('users.urls')),
    path('productos/', include('productos.urls')),
    path('categoria/', include('categoria.urls')),
]