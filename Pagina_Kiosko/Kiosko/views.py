from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Producto, Venta, Cliente
from .forms import ProductoForm, VentaForm, ClienteForm

# Create your views here.

def home(request):
    return render(request, 'Kiosko/home.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'Kiosko/productos_lista.html', {'productos':productos})


def buscar_producto(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre_producto__icontains=query)

    return render(request, 'Kiosko/buscar_producto.html', {'productos': productos, 'query': query})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'Kiosko/agregar_producto.html', {'form': form})

def buscar_venta(request):
    query = request.GET.get('q','')
    ventas = Venta.objects.filter(
    Q(cliente__nombre__icontains=query) |
    Q(producto__nombre_producto__icontains=query) |
    Q(fecha__icontains=query)
    )
    return render(request, 'Kiosko/buscar_venta.html',{'ventas':ventas, 'query':query})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'Kiosko/ventas_lista.html', {'ventas': ventas})

def agregar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
        
    else:
        form = VentaForm()
    return render(request, 'Kiosko/agregar_venta.html',{'form':form})

def buscar_cliente(request):
    query = request.GET.get('q', '') 
    clientes = Cliente.objects.filter(
        Q(nombre__icontains=query) | 
        Q(email__icontains=query) |
        Q(telefono__icontains=query)
    )
    return render(request, 'Kiosko/buscar_cliente.html', {'clientes': clientes, 'query': query})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'Kiosko/clientes_lista.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'Kiosko/agregar_cliente.html', {'form': form})