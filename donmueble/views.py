from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def productos(request):
    return render(request, 'productos.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def clientes(request):
    return render(request, 'clientes.html')