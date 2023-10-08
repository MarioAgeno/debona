from django import forms
from .models import Provincia, Clientes, ClientesSaldos, Lista, stockMedidaView

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = [
              'nombre',
              'id',
              'codafip'
        ]

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
              'id',
              'nombre',
              'domicilio',
              'barrio',
              'idlocalidad',
              'idtipopersona',
              'idtipodoc',
              'documento',
              'idcodiva',
              'cuit',
              'ingbruto',
              'telefono',
              'telefono2',
              'celular',
              'idzona',
              'fnacimiento',
              'email',
              'email2',
              'transporte',
              'idvendedor',
              'sexo',
              'idactividad',
              'idsucursal',
              'idpercible',
              'vip',
              'mayorista',
              'ctacte',
              'subcuenta',
              'observacion',
        ]
# Asociar los widgets a los campos que lo requieren (opcional) 
        widgets = {
             'idlocalidad': forms.Select(attrs={'class': 'form-control form-select'}), 
             'idtipopersona': forms.Select(attrs={'class': 'form-control form-select'}),
             'idtipodoc': forms.Select(attrs={'class': 'form-control form-select'}),
             'idcodiva': forms.Select(attrs={'class': 'form-control form-select'}), 
             'idzona': forms.Select(attrs={'class': 'form-control form-select'}), 
             'idvendedor': forms.Select(attrs={'class': 'form-control form-select'}), 
             'idactividad': forms.Select(attrs={'class': 'form-control form-select'}), 
             'idsucursal': forms.Select(attrs={'class': 'form-control form-select'}), 
             'idpercible': forms.Select(attrs={'class': 'form-control form-select'}), 
             'ctacte': forms.CheckboxInput(attrs={'class': 'form-control form-check-input'}), 
             'vip': forms.CheckboxInput(attrs={'class': 'form-control form-check-input'}), 
             'mayorista': forms.CheckboxInput(attrs={'class': 'form-control form-check-input'}), 
             'observacion': forms.Textarea(attrs={'class': 'form-control form-row-3'}), 
             'sexo': forms.RadioSelect(attrs={'class': 'from-control form-radio-selected'}),
             }

class ClienteSaldoForm(forms.ModelForm):
    class Meta:
        model = ClientesSaldos
        fields = [
            #'idcliente',
            'nombre',
            'saldo'
        ]

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = [
              'medida',
              'cai',
              'nombre',
              'idfamilia',
              'idmarcar',
              'idmodelo',
              'idestado'
        ]

class stockMedidaViewForm(forms.ModelForm):
    class Meta:
        model = stockMedidaView
        fields = [
            'id',
            'stock',
            'nombre',
            'minimo',
            'estado'
        ]