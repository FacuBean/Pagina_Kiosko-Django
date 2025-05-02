from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from .models import Producto, Venta, Cliente
from .forms import ProductoForm, VentaForm, ClienteForm

# Codigo entrega final {
def solo_superusuarios(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)
#}

def home(request):
    return render(request, 'Kiosko/home.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'Kiosko/productos_lista.html', {'productos':productos})


def buscar_producto(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre_producto__icontains=query)

    return render(request, 'Kiosko/buscar_producto.html', {'productos': productos, 'query': query})

@solo_superusuarios
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'Kiosko/agregar_producto.html', {'form': form})
    
@solo_superusuarios
def buscar_venta(request):
    query = request.GET.get('q','')
    ventas = Venta.objects.filter(
    Q(cliente__nombre__icontains=query) |
    Q(producto__nombre_producto__icontains=query) |
    Q(fecha__icontains=query)
    )
    return render(request, 'Kiosko/buscar_venta.html',{'ventas':ventas, 'query':query})

@solo_superusuarios
def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'Kiosko/ventas_lista.html', {'ventas': ventas})

@solo_superusuarios
def agregar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            cliente = Cliente.objects.get(user=request.user)
            venta.cliente = cliente
            venta.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'Kiosko/agregar_venta.html', {'form': form})

@solo_superusuarios
def buscar_cliente(request):
    query = request.GET.get('q', '') 
    clientes = Cliente.objects.filter(
        Q(nombre__icontains=query) | 
        Q(email__icontains=query) |
        Q(telefono__icontains=query)
    )
    return render(request, 'Kiosko/buscar_cliente.html', {'clientes': clientes, 'query': query})

@solo_superusuarios
def lista_clientes(request):
    clientes = User.objects.all()
    return render(request, 'Kiosko/clientes_lista.html', {'clientes': clientes})

@solo_superusuarios
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'Kiosko/agregar_cliente.html', {'form': form})


#Codigo de entrega final

def acerca_de_mi(request):
    return render(request, 'Kiosko/acerca_de_mi.html')

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Kiosko/producto_form.html'
    success_url = reverse_lazy('lista_productos')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'Kiosko/eliminar_producto.html'
    success_url = reverse_lazy('lista_productos')

class VentaUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'Kiosko/editar_venta.html'
    success_url = reverse_lazy('lista_ventas')

class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'Kiosko/eliminar_venta.html'
    success_url = reverse_lazy('lista_ventas')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'Kiosko/editar_cliente.html'
    success_url = reverse_lazy('lista_clientes')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'Kiosko/eliminar_cliente.html'
    success_url = reverse_lazy ('lista_clientes')

def detalle_cliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    return render(request, 'Kiosko/detalle_cliente.html',{'cliente':cliente})