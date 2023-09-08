from django.contrib import admin

# Register your models here.
from .models import *

#admin.site.register(Provincia)
@admin.register(Provincia)
class ProviniasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'codafip')
    ordering = ('id',)
    search_fields = ('nombre',)
    #list_editable = ('nombre', 'codAFIP')
    list_display_links = ('nombre', )
    #list_filter = ('id', )
    #list_per_page = 25
    #save_on_top = True

admin.site.register(Localidad)
admin.site.register(Sucursal)
admin.site.register(Codven)
admin.site.register(Empresa)
admin.site.register(Parametros)
admin.site.register(Monedas)
admin.site.register(Familias)
admin.site.register(Modelos)
admin.site.register(Marcas)
admin.site.register(Zonas)
admin.site.register(Listaestados)
admin.site.register(Listadespachos)
admin.site.register(Stock)
admin.site.register(Medidasestados)
admin.site.register(Tipopersona)
admin.site.register(Tipodoc)
admin.site.register(Operarios)
admin.site.register(Actividad)
admin.site.register(Codiva)
admin.site.register(Tpercepib)
admin.site.register(Treten)
admin.site.register(Vendedor)
admin.site.register(ClientesResumenPendiente)

#admin.site.register(Lista)
@admin.register(Lista)
class ListaAdmin(admin.ModelAdmin):
    list_display = ('cai', 'medida', 'nombre', 'idmarcar')
    ordering = ('medida',)
    search_fields = ('medida',)
    #list_editable = ('nombre', 'codAFIP')
    list_display_links = ('nombre', )
    list_filter = ('idmarcar', 'idfamilia', 'idmodelo',)
    list_per_page = 50
    #save_on_top = True

#admin.site.register(Clientes)
@admin.register(Clientes)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'domicilio', 'idlocalidad')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_display_links = ('nombre',)
    list_filter = ('idlocalidad', 'idzona', 'idvendedor', )
    list_per_page = 50

#admin.site.register(ClientesSaldos)
@admin.register(ClientesSaldos)
class ClientesSaldosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'saldo')
    ordering = ('nombre',)
    search_fields = ('nombre',)
    list_display_links = ('nombre',)
    list_per_page = 50

