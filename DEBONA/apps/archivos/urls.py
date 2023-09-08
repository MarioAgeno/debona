from django.urls import path

from .views import provincia_listar, provincia_agregar, provincia_editar, provincia_eliminar
from .views import cliente_listar, cliente_agregar, cliente_editar, cliente_eliminar
from .views import clientesaldo_listar, clientesaldo_solo, clienteresumenpendiente_listar



urlpatterns = [
	#-- Provincias.
	path('provincia/listar/', provincia_listar, name="provincia_listar"),
	path('provincia/agregar/<str:accion>/', provincia_agregar, name="provincia_agregar"),
	path('provincia/editar/<int:id>/<str:accion>/', provincia_editar, name="provincia_editar"),
	path('provincia/eliminar/<int:id>/', provincia_eliminar, name='provincia_eliminar'),
	#-- Clientes.
	path('cliente/listar/', cliente_listar, name="cliente_listar"),
	path('cliente/agregar/<str:accion>/', cliente_agregar, name="cliente_agregar"),
	path('cliente/editar/<int:id>/<str:accion>/', cliente_editar, name="cliente_editar"),
	path('cliente/eliminar/<int:id>/', cliente_eliminar, name='cliente_eliminar'),
	#-- Clientes Saldos.
	path('cliente/listarsaldos/', clientesaldo_listar, name="clientesaldo_listar"),
   	#-- Clientes Resumen Pendiente.
	#path('cliente/clienteresumen_listar/<int:id>', clienteresumen_listar, name="clienteresumen_listar"),
	path('cliente/clientesaldo_solo/<int:id>', clientesaldo_solo, name="clientesaldo_solo"),
	path('cliente/clienteresumenpendiente_listar/<int:id>', clienteresumenpendiente_listar, name="clienteresumenpendiente_listar"),
]