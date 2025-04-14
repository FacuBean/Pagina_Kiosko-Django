from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/buscar/', views.buscar_producto, name='buscar_producto'),
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('ventas/agregar/', views.agregar_venta, name='agregar_venta'),
    path('buscar_venta/', views.buscar_venta, name='buscar_venta'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('buscar_cliente/', views.buscar_cliente, name='buscar_cliente'),
]
