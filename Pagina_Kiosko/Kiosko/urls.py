from django.urls import path, include
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

    #Codigo entrega final
    path('about/', views.acerca_de_mi, name='acerca_de_mi'),
    path('producto/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='editar_producto'),
    path('producto/<int:pk>/borrar/', views.ProductoDeleteView.as_view(), name='borrar_producto'),
    path('venta/<int:pk>/editar/', views.VentaUpdateView.as_view(), name='editar_venta'),
    path('venta/<int:pk>/borrar/', views.VentaDeleteView.as_view(), name='borrar_venta'),
    path('cliente/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='editar_cliente'),
    path('cliente/<int:pk>/borrar/', views.ClienteDeleteView.as_view(), name='borrar_cliente'),

    path('clientes/<int:pk>/', views.detalle_cliente, name='detalle_cliente'),

    path('usuarios/', include('usuarios.urls')),
]
