from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventas_view, name='Ventas'),
    path('clientes/',views.clientes_view, name='Clientes'),
    path('add_cliente/',views.add_cliente_view, name='AddCliente'),
    path('edit_cliente/',views.edit_cliente_view, name='EditCliente'),
    path('delete_cliente/',views.delete_cliente_view, name='DeleteCliente'),
    path('productos/',views.productos_view, name='Productos'),
    path('add_producto/',views.add_producto_view, name='AddProducto'),
    ]