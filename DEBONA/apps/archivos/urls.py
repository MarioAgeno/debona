from django.urls import path

from .views import provincia_listar, provincia_agregar, provincia_editar, provincia_eliminar
from .views import cliente_listar, cliente_agregar, cliente_editar, cliente_eliminar, cliente_listar_crud
from .views import clientesaldo_listar, clientesaldo_solo, clienteresumenpendiente_listar
from .views import lista_listar, lista_agregar, lista_editar, lista_eliminar, stockmedida



urlpatterns = [
	#-- Provincias.
	path('provincia/listar/', provincia_listar, name="provincia_listar"),
	path('provincia/agregar/<str:accion>/', provincia_agregar, name="provincia_agregar"),
	path('provincia/editar/<int:id>/<str:accion>/', provincia_editar, name="provincia_editar"),
	path('provincia/eliminar/<int:id>/', provincia_eliminar, name='provincia_eliminar'),
	#-- Lista de Productos
	path('lista/listar/', lista_listar, name="lista_listar"),
	path('lista/agregar/<str:accion>/', lista_agregar, name="lista_agregar"),
	path('lista/editar/<int:id>/<str:accion>/', lista_editar, name="lista_editar"),
	path('lista/eliminar/<int:id>/', lista_eliminar, name='lista_eliminar'),
	path('lista/stockmedida/<int:id>', stockmedida, name="stockmedida"),

	#-- Clientes.
	path('cliente/listar/', cliente_listar, name="cliente_listar"),
	path('cliente/cliente_listar_crud/', cliente_listar_crud, name="cliente_listar_crud"),
	path('cliente/agregar/<str:accion>/', cliente_agregar, name="cliente_agregar"),
	path('cliente/editar/<int:id>/<str:accion>/', cliente_editar, name="cliente_editar"),
	path('cliente/eliminar/<int:id>/', cliente_eliminar, name='cliente_eliminar'),
	#-- Clientes Saldos.
	path('cliente/listarsaldos/', clientesaldo_listar, name="clientesaldo_listar"),

   	#-- Clientes Saldo Individual y Resumen Pendiente
	#path('cliente/clienteresumen_listar/<int:id>', clienteresumen_listar, name="clienteresumen_listar"),
	path('cliente/clientesaldo_solo/<int:id>', clientesaldo_solo, name="clientesaldo_solo"),
	path('cliente/clienteresumenpendiente_listar/<int:id>', clienteresumenpendiente_listar, name="clienteresumenpendiente_listar"),


]
