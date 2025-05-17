from django.urls import path
from .views import index, contacto, productos, nosotros, clientes

urlpatterns = [
    path('', index,name='index'),
    path('contacto/', contacto,name='contacto'),
    path('productos/', productos,name='productos'),
    path('nosotros/', nosotros, name='nosotros'),
    path('clientes/', clientes, name='clientes'),
]
