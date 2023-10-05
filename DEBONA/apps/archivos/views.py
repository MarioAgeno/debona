from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from . models import *
from . import forms


# Create your views here.
#-- Provincia -----------------------------------------------------------------------
#-- Vista que lista las Provincias
def provincia_listar(request):
	#-- Obtener el texto para filtrar.
	text = request.GET.get('buscar', '')
	
	#-- Realizar el filtro según el contenido de text.
	provincia_lst = Provincia.objects.filter(nombre__icontains=text)

	#-- Aplicar la paginación (8 items por página).
	provincia_pag = Paginator(provincia_lst, 8)
	
	#-- Establecer la página a mostrar, por defecto la primera página.
	page = request.GET.get('page', 1)
	
	#-- Obtener los ítems de la página indicada.
	provincias = provincia_pag.get_page(page)
	
	#-- Preparar el contexto a pasar a la plantilla.
	context = {
		'provincias': provincias,
		'paginator': provincia_pag,
		'buscar': text
	}
	
	#-- Renderizar la plantilla y su contexto.
	return render(request, 'archivos/provincia/listar.html', context)

#-- Vista que permiter Agregar una nueva Provincia
def provincia_agregar(request, accion):
	if request.method == 'POST':
		#-- Si se ha llamado la vista con el botón "guardar" desde la plantilla.
		
		#-- Instanciar un objeto form con los datos en la platilla.
		form = forms.ProvinciaForm(request.POST)
		
		#-- Validar los datos.
		if form.is_valid():
			#-- Agregar un nuevo registro en la BBDD.
			form.save()
			#-- Redireccionar a la lista de provincias.
			return redirect('provincia_listar')
	else:
		#-- Si se ha llamado a la vista con el botón "Agregar nueva".
		
		#-- Instanciar un objeto form con los datos en blanco y/o por defecto.
		form = forms.ProvinciaForm()
	
	#-- Renderizar el formulario de provincias con su contexto.
	return render(request, 'archivos/provincia/form.html', {'form': form, 'accion': accion})

#-- Vista que permite Modificar los datos de una Provincia
def provincia_editar(request, id, accion):
	#-- Obtener la instancia de la provincia a modificar selecionada desde la lista de provincias (botón editar).
	provincia = Provincia.objects.get(id=id)
	if request.method == 'GET':
		#-- Cuando se ha llamado a esta vista con el botón de editar desde la lista de provincias.
		
		#-- Instanciar un objeto form con los datos de la provincia a modificar.
		form = forms.ProvinciaForm(instance=provincia)
	else:
		#-- Cuando se ha llamado a esta vista con el botón "Guardar" desde el form de provincia.
		
		#-- Instanciar un ojeto form con los datos en el formulario html de la instancia a modificar.
		form = forms.ProvinciaForm(request.POST, instance=provincia)
		
		#-- Validar los datos.
		if form.is_valid():
			#-- Actualizar los datos de la provincia en la BBDD.
			form.save()
			#-- Redireccionar a la lista de provincias.
			return redirect('provincia_listar')
	
	#-- Renderizar el formulario de provincias con su contexto.
	return render(request, 'archivos/provincia/form.html', {'form': form, 'accion': accion})

#-- Vista que permite Eliminar una Provincia
def provincia_eliminar(request, id):
	#-- Obtener la instancia de la provincia a eliminar selecionada desde la lista de provincias (botón eliminar).
	provincia = Provincia.objects.get(id=id)
	if request.method == 'POST':
		#-- Si se ha llamado esta vista con el botón "Elimiar" desde la página de confirmación.
		
		#-- Eliminar la instancia de la provincia de la BBDD.
		provincia.delete()
		
		#-- Redireccionar a la lista de provincias.
		return redirect('provincia_listar')
	
	#-- Si es llamada esta vista con el método GET, mostrar la confirmación de la provincia a elimiar.
	return render(request, 'archivos/provincia/eliminar.html', {'provincia': provincia})

#-- Clientes lista para Editar (CRUD) -------------------------------------------------------------
def cliente_listar_crud(request):
	text = request.GET.get('buscar', '')
	clientes_lst = Clientes.objects.filter(
		Q(nombre__icontains=text) |
		Q(cuit__icontains=text)
		)
	clientes_pag = Paginator(clientes_lst, 25)
	page = request.GET.get('page', 1)
	clientes = clientes_pag.get_page(page)
	
	#-- Preparar el contexto a pasar a la plantilla.
	context = {
		'clientes': clientes,
		'paginator': clientes_pag,
		'buscar': text
	}
	return render(request, 'archivos/cliente/listar_crud.html', context)


#-- Clientes -----------------------------------------------------------------------
#-- Vista que lista las Clientes
def cliente_listar(request):
	text = request.GET.get('buscar', '')
	clientes_lst = Clientes.objects.filter(
		Q(nombre__icontains=text) |
		Q(cuit__icontains=text)
		)
	clientes_pag = Paginator(clientes_lst, 25)
	page = request.GET.get('page', 1)
	clientes = clientes_pag.get_page(page)
	
	#-- Preparar el contexto a pasar a la plantilla.
	context = {
		'clientes': clientes,
		'paginator': clientes_pag,
		'buscar': text
	}
	return render(request, 'archivos/cliente/listar.html', context)

#-- Vista que permiter Agregar un nueva Cliente
def cliente_agregar(request, accion):
	if request.method == 'POST':
		form = forms.ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('cliente_listar_crud')
	else:
		form = forms.ClienteForm()
	return render(request, 'archivos/cliente/form.html', {'form': form, 'accion': accion})

#-- Vista que permite Modificar los datos de un Cliente
def cliente_editar(request, id, accion):
	cliente = Clientes.objects.get(id=id)
	if request.method == 'GET':
		form = forms.ClienteForm(instance=cliente)
	else:
		form = forms.ClienteForm(request.POST, instance=cliente)
		if form.is_valid():
			form.save()
			return redirect('cliente_listar_crud')
	return render(request, 'archivos/cliente/form.html', {'form': form, 'accion': accion})

#-- Vista que permite Eliminar un Cliente
def cliente_eliminar(request, id):
	cliente = Clientes.objects.get(id=id)
	if request.method == 'POST':
		cliente.delete()
		return redirect('cliente_listar')
	return render(request, 'archivos/cliente/eliminar.html', {'cliente': cliente})

#-- Clientes Saldos-----------------------------------------------------------------------
#-- Vista que lista las Clientes con Saldos
def clientesaldo_listar(request):
	text = request.GET.get('buscar', '')
	saldos_lst = ClientesSaldos.objects.filter(nombre__icontains=text)
	saldos_pag = Paginator(saldos_lst, 25)
	page = request.GET.get('page', 1)
	saldos = saldos_pag.get_page(page)
	
	#-- Preparar el contexto a pasar a la plantilla.
	context = {
		'saldos': saldos,
		'paginator': saldos_pag,
		'buscar': text
	}
	return render(request, 'archivos/cliente/listarsaldos.html', context)

#-- Clientes Resumen -----------------------------------------------------------------------
#-- Vista de Resumen Pendiente de Clientes
def clientesaldo_solo(request, id):
	resumen_lst = ClientesSaldos.objects.filter(idcliente=id)
	resumen_pag = Paginator(resumen_lst,25)
	page = request.GET.get('page', 1)
	saldo = resumen_pag.get_page(page)

	context = {
		'saldo': saldo,
		'paginator': resumen_pag
	}
	return render(request, 'archivos/cliente/clientesaldo_solo.html', context)

#-- Clientes Resumen -----------------------------------------------------------------------
#-- Vista de Resumen Pendiente de Clientes
def clienteresumenpendiente_listar(request, id):
	resumen_lst = ClientesResumenPendiente.objects.filter(idcliente=id)
	resumen_pag = Paginator(resumen_lst,25)
	page = request.GET.get('page', 1)
	resumen = resumen_pag.get_page(page)

	context = {
		'resumen': resumen,
		'paginator': resumen_pag
	}
	return render(request, 'archivos/cliente/clienteresumenpendiente_listar.html', context)


#-- Lista de productos  -----------------------------------------------------------------------
#-- Vista que lista los productos
def lista_listar(request):
	text = request.GET.get('buscar', '')
	lista_lst = Lista.objects.filter(
		Q(medida__icontains=text) |
		Q(cai__icontains=text)
		)
	lista_pag = Paginator(lista_lst, 20)
	page = request.GET.get('page', 1)
	listas = lista_pag.get_page(page)
	
	#-- Preparar el contexto a pasar a la plantilla.
	context = {
		'listas': listas,
		'paginator': lista_pag,
		'buscar': text
	}
	
	return render(request, 'archivos/lista/listar.html', context)

#-- Vista que permiter Agregar un nuevo Producto
def lista_agregar(request, accion):
	if request.method == 'POST':
		form = forms.ListaForm(request.POST)
		
		#-- Validar los datos.
		if form.is_valid():
			form.save()
			return redirect('lista_listar')
	else:
		form = forms.ListaForm()
	
	return render(request, 'archivos/lista/form.html', {'form': form, 'accion': accion})

#-- Vista que permite Modificar los datos de un Producto
def lista_editar(request, id, accion):
	lista = Lista.objects.get(id=id)
	if request.method == 'GET':
		form = forms.ListaForm(instance=lista)
	else:
		form = forms.ListaForm(request.POST, instance=lista)
		
		if form.is_valid():
			form.save()
			return redirect('lista_listar')
	
	return render(request, 'archivos/lista/form.html', {'form': form, 'accion': accion})

#-- Vista que permite Eliminar un Producto de la Lista
def lista_eliminar(request, id):
	lista = Lista.objects.get(id=id)
	if request.method == 'POST':
		lista.delete()
		return redirect('lista_listar')
	
	#-- Si es llamada esta vista con el método GET, mostrar la confirmación del producto a elimiar.
	return render(request, 'archivos/lista/eliminar.html', {'lista': lista})

#-- Stock por Medida -----------------------------------------------------------------------
#-- Vista de Stock por Medida
def stockmedida(request, id):
	resumen_lst = stockMedidaView.objects.filter(idlista=id)
	resumen_pag = Paginator(resumen_lst,25)
	page = request.GET.get('page', 1)
	resumen = resumen_pag.get_page(page)

	context = {
		'resumen': resumen,
		'paginator': resumen_pag
	}
	return render(request, 'archivos/lista/stockmedida.html', context)
