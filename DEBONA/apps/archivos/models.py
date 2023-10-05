from django.db import models

# Create your models here.

class Provincia(models.Model):
    #id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=25)
    codafip = models.CharField('Codigo AFIP', db_column='codAFIP', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provincias'
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Localidad(models.Model):
    codpostal = models.CharField('Codigo Postal', primary_key=True, max_length=5)
    nombre = models.CharField(max_length=25)
    idProvincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, db_column='idProvincia', verbose_name="Provincia")
    codafip = models.CharField('Codigo AFIP', db_column='codAFIP', max_length=5, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'localidad'
        verbose_name = ('Localidad')
        verbose_name_plural = ('Localidades')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre + ' - ' + self.idProvincia.nombre


class Sucursal(models.Model):
#    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    idLocalidad = models.ForeignKey(Localidad, models.PROTECT, db_column='idLocalidad', verbose_name="Localidad")
    telefonos = models.CharField(max_length=30)
    eMail = models.CharField(max_length=50, blank=True, null=True)
    inicioActividad = models.DateField('Inicio de Actividad', blank=True, null=True)
    codMichelin = models.CharField('Codigo Michelin', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'
        verbose_name = ('Sucursal')
        verbose_name_plural = ('Sucursales')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Codven(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    nombre = models.CharField(max_length=25)
    multven = models.SmallIntegerField('Mult. Ventas', db_column='multVen', blank=True, null=True)  # Field name made lowercase.
    multcli = models.SmallIntegerField('Mult. Clientes', db_column='multCli', blank=True, null=True)  # Field name made lowercase.
    multsto = models.SmallIntegerField('Mult. Stock', db_column='multSto', blank=True, null=True)  # Field name made lowercase.
    multcaja = models.SmallIntegerField('Mult. Caja', db_column='multCaja', blank=True, null=True)  # Field name made lowercase.
    multest = models.SmallIntegerField('Mult. Estadisticas', db_column='multEst', blank=True, null=True)  # Field name made lowercase.
    multcom = models.SmallIntegerField('Mult. Compensada', db_column='multCom', blank=True, null=True)  # Field name made lowercase.
    letra = models.CharField('Letra Principal', max_length=1)
    letra2 = models.CharField('Letra Secundaria', max_length=1)
    calciva = models.BooleanField('Calcula IVA', db_column='calcIVA')  # Field name made lowercase.
    libroiva = models.BooleanField('Libro IVA', db_column='libroIVA')  # Field name made lowercase.
    fiscal = models.BooleanField('Comp.Fiscal')
    nofiscal = models.BooleanField('Comp.No Fiscal', db_column='noFiscal')  # Field name made lowercase.
    electronica = models.BooleanField('Comp.Electronico', db_column='Electronica')  # Field name made lowercase.
    facturacion = models.BooleanField('Mostrar en Facturacion')
    pendiente = models.BooleanField('Mostrar en Pendiente')
    presupuesto = models.BooleanField('Es Presupuesto')
    codafipa = models.CharField('Codigo AFIP A', db_column='codAFIPA', max_length=3)  # Field name made lowercase.
    codafipb = models.CharField('Codigo AFIP B', db_column='codAFIPB', max_length=3)  # Field name made lowercase.
    compasoc = models.CharField('Codigo AFIP C', db_column='compAsoc', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'codven'
        verbose_name = ('Codigos de Venta')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Empresa(models.Model):
    #id = models.IntegerField(primary_key=True)
    #id = models.AutoField(primary_key=True)
    razonsocial = models.CharField('Razon Social', db_column='RazonSocial', max_length=50)  # Field name made lowercase.
    nombrefantasia = models.CharField('Nombre de Fantasia', db_column='NombreFantasia', max_length=50)  # Field name made lowercase.
    domicilio = models.CharField(max_length=40)
    codpostal = models.CharField('Codigo Postal', max_length=5)
    localidad = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    condiva = models.CharField(db_column='condIVA', max_length=20)  # Field name made lowercase.
    cbu = models.CharField('CBU', max_length=22, blank=True, null=True)
    cbualias = models.CharField('Alias CBU', db_column='cbuAlias', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cuit = models.DecimalField('CUIT', max_digits=11, decimal_places=0)
    ingbrutos = models.CharField('Ing. Bruto', db_column='ingBrutos', max_length=15, blank=True, null=True)  # Field name made lowercase.
    inicioactividad = models.DateField('Inicio Activdad', db_column='inicioActividad', blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=50, blank=True, null=True)
    web = models.CharField(max_length=50, blank=True, null=True)
    logo = models.TextField(blank=True, null=True) 
    wsarchcrt = models.CharField('Archivo WSFE CRT', db_column='wsArchCRT', max_length=50, blank=True, null=True) 
    wsarchkey = models.CharField('Archivov WSFE KEY', db_column='wsArchKEY', max_length=50, blank=True, null=True)
    wstoken = models.TextField('Token WSFE', db_column='wsToken', blank=True, null=True)
    wssign = models.TextField('Sign WSFE', db_column='wsSign', blank=True, null=True)
    wsexpiracion = models.DateTimeField('Expiracion Tiket WSFE', db_column='wsExpiracion', blank=True, null=True)  # Field name made lowercase.
    wsmodo = models.IntegerField('WSFE en Produccion', db_column='wsModo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'
        verbose_name = ('Datos de la Empresa')

    def __str__(self):
        return self.razonsocial
    
class Parametros(models.Model):
    idempresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, db_column='idEmpresa', verbose_name="Empresa")
    #idempresa = models.IntegerField('Empresa', db_column='idEmpresa', primary_key=True)  # Field name made lowercase.
    interes = models.DecimalField('Tasa de Interes', max_digits=6, decimal_places=2)
    dolar = models.DecimalField('Cotizacion Dolar', max_digits=10, decimal_places=4)
    cierreventas = models.DateField('Cierre de Ventas')
    descmax = models.DecimalField('Descuento Maximo', db_column='DescMax', max_digits=6, decimal_places=2)  # Field name made lowercase.
    permitedesc = models.BooleanField('Permite Descuentos', db_column='PermiteDesc')  # Field name made lowercase.
    permiteprecio = models.BooleanField('Cambiar Precios', db_column='PermitePrecio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parametros'
        verbose_name = ('Parametros del Sistema')

    def __str__(self):
        return self.idempresa
    
class Monedas(models.Model):
    nombre = models.CharField(max_length=20)
    simbolo = models.CharField(max_length=3)
    cotizacion = models.DecimalField(max_digits=10, decimal_places=5)
    predeterminada = models.BooleanField()
    codafip = models.CharField('Codigo AFIP', db_column='codAFIP', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monedas'
        verbose_name = ('Moneda')
        verbose_name_plural = ('Monedas')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Familias(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    comisionop = models.DecimalField('Comision Operario', db_column='comisionOP', max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'familias'
        verbose_name = ('Familia')
        verbose_name_plural = ('Familias de Productos')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
class Marcas(models.Model):
    #id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    idmoneda = models.ForeignKey('Monedas', models.PROTECT, db_column='idMoneda')  # Field name made lowercase.
    otras = models.BooleanField('Otras Marcas')

    class Meta:
        managed = False
        db_table = 'marcas'
        verbose_name = ('Marca')
        verbose_name_plural = ('Marcas')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Modelos(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'modelos'
        verbose_name = ('Modelo')
        verbose_name_plural = ('Modelos de Productos')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
class Listaestados(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'listaEstados'
        verbose_name = ('Estado')
        verbose_name_plural = ('Estados de Productos')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Medidasestados(models.Model):
    idlista = models.IntegerField(db_column='idLista')  # Field name made lowercase.
    idestado = models.CharField(db_column='idEstado', max_length=1)  # Field name made lowercase.
    minimo = models.IntegerField()
    maximo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'MedidasEstados'
        unique_together = (('idlista', 'idestado'),)
        verbose_name = ('Estados de Medidas')
        verbose_name_plural = ('Estados de Medidas')
        ordering = ['idlista']

    def __str__(self):
        return self.idlista   

class Lista(models.Model):
    #id = models.AutoField(primary_key=True)
    idfamilia = models.ForeignKey(Familias, models.PROTECT, db_column='idFamilia', verbose_name='Familia') 
    idmarcar = models.ForeignKey('Marcas', models.PROTECT, db_column='idMarcar', verbose_name='Marca') 
    idmodelo = models.ForeignKey('Modelos', models.PROTECT, db_column='idModelo', verbose_name='Modelo') 
    segmento = models.CharField(max_length=3)
    cai = models.CharField(max_length=15)
    medida = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1)
    costo = models.DecimalField(max_digits=12, decimal_places=2)
    aliciva = models.DecimalField('IVA', db_column='alicIVA', max_digits=6, decimal_places=2)  # Field name made lowercase.
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    idestado = models.CharField('Estado', db_column='idEstado', max_length=1)  # Field name made lowercase.
    descuento = models.DecimalField(max_digits=6, decimal_places=2)
    minimo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lista'
        verbose_name = ('Lista de Precios')
        verbose_name_plural = ('Lista de Precios')
        ordering = ['medida']

    def __str__(self):
        return self.medida+'- '+ self.nombre

class Listadespachos(models.Model):
    idlista = models.ForeignKey(Lista, models.CASCADE, db_column='idLista')  # Field name made lowercase.
    despacho = models.CharField(max_length=16)
    fecha = models.DateField()
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'listaDespachos'
        verbose_name = ('Nro.Despacho')
        verbose_name_plural = ('Nro.Despachos')
        ordering = ['idlista']

    def __str__(self):
        return self.idlista   

class Stock(models.Model):
    idlista = models.OneToOneField(Lista, models.PROTECT, db_column='idLista', primary_key=True)  # Field name made lowercase. The composite primary key (idLista, idSucursal) found, that is not supported. The first column is selected.
    idsucursal = models.ForeignKey('Sucursal', models.PROTECT, db_column='idSucursal')  # Field name made lowercase.
    stock = models.IntegerField()
    minimo = models.IntegerField()
    maximo = models.IntegerField()
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stock'
        unique_together = (('idlista', 'idsucursal'), ('idsucursal', 'idlista'),)

    def __str__(self):
        return self.idlista  
    

class Zonas(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'zonas'
        verbose_name = ('Zona')
        verbose_name_plural = ('Zonas')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Tipopersona(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipoPersona'
        verbose_name = ('Tipo de Persona')
        ordering = ['nombre']
 
    def __str__(self):
        return self.nombre

class Tipodoc(models.Model):
    tipodoc = models.CharField(db_column='tipoDoc', primary_key=True, max_length=4)  # Field name made lowercase.
    codafip = models.CharField(db_column='codAFIP', max_length=2)  # Field name made lowercase.
    codhasar = models.CharField(db_column='codHASAR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    codepson = models.CharField(db_column='codEPSON', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipodoc'
        verbose_name = ('Tipo de Documento')
        verbose_name_plural = ('Tipo de Documentos')
        ordering = ['tipodoc']

    def __str__(self):
        return self.tipodoc
    
class Operarios(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'operarios'
        verbose_name = ('Operario')
        verbose_name_plural = ('Operarios')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre        
    

class Actividad(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'actividad'
        verbose_name = ('Actividad')
        verbose_name_plural = ('Actividades de Clientes')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre  
    
class Codiva(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    nombre = models.CharField(max_length=20)
    discrimina = models.BooleanField(blank=True, null=True)
    codepson = models.CharField(db_column='codEPSON', max_length=2, blank=True, null=True)  # Field name made lowercase.
    codhasar = models.CharField(db_column='codHASAR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    codafip = models.CharField(db_column='codAFIP', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'codIVA'
        verbose_name = ('Codigo de IVA')
        verbose_name_plural = ('Codigos de IVA')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre 

class Tpercepib(models.Model):
    nombre = models.CharField(max_length=30)
    alicuota = models.DecimalField(max_digits=6, decimal_places=2)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    minimo = models.DecimalField(max_digits=12, decimal_places=2)
    discrimina = models.BooleanField()
    gravadototal = models.SmallIntegerField(db_column='GravadoTotal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tPercepIB'
        verbose_name = ('Percepcion IIBB')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre 
    
class Treten(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tReten'
        verbose_name = ('Tabla de Retenciones')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre 


class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    idsucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT, db_column='idSucursal')  # Field name made lowercase.
    diasgracia = models.IntegerField(db_column='diasGracia')  # Field name made lowercase.
    diasrtos = models.IntegerField(db_column='diasRtos')  # Field name made lowercase.
    tipo = models.CharField(max_length=1)
    emailfac = models.BooleanField(db_column='eMailFac')  # Field name made lowercase.
    emailsdo = models.BooleanField(db_column='eMailSdo')  # Field name made lowercase.
    emailest = models.BooleanField(db_column='eMailEst')  # Field name made lowercase.
    pjeauto = models.DecimalField(db_column='pjeAuto', max_digits=6, decimal_places=2)  # Field name made lowercase.
    pjecamion = models.DecimalField(db_column='pjeCamion', max_digits=6, decimal_places=2)  # Field name made lowercase.
    coldcto = models.SmallIntegerField(db_column='colDcto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vendedor'
        verbose_name = ('Vendedor')
        verbose_name_plural = ('Vendedores')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre 


class Clientes(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    nombre = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    barrio = models.CharField(max_length=30)
    idlocalidad = models.ForeignKey(Localidad, models.PROTECT, db_column='idLocalidad', verbose_name='Localidad')
    idtipopersona = models.ForeignKey(Tipopersona, models.PROTECT, db_column='idTipoPersona', verbose_name='Tipo de Persona')
    idtipodoc = models.ForeignKey(Tipodoc, models.PROTECT, db_column='idTipodoc', verbose_name='Tipo de Documento')
    documento = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
    idcodiva = models.ForeignKey(Codiva, models.PROTECT, db_column='idCodiva', verbose_name='Codigo de IVA')
    cuit = models.DecimalField(db_column='CUIT', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ingbruto = models.CharField(db_column='ingBruto', max_length=15, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(max_length=15)
    telefono2 = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15)
    idzona = models.ForeignKey(Zonas, verbose_name='Zona', on_delete=models.PROTECT, db_column='idZona')
    fnacimiento = models.DateField(db_column='fNacimiento', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='eMail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email2 = models.CharField(db_column='eMail2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    transporte = models.CharField(max_length=30, blank=True, null=True)
    idvendedor = models.ForeignKey(Vendedor, models.PROTECT, db_column='idvendedor', verbose_name='Vendedor')
    sexo = models.CharField("Sexo", max_length=1, choices=SEXO, null=False, blank=False)
    idactividad = models.ForeignKey(Actividad, models.PROTECT, db_column='idActividad', verbose_name='Actividad')
    idsucursal = models.ForeignKey(Sucursal, models.PROTECT, db_column='idSucursal', verbose_name='Sucursal')
    idpercible = models.ForeignKey(Tpercepib, models.PROTECT, db_column='idPercIB', verbose_name='Percepcion IIBB')
    vip = models.BooleanField(db_column='VIP', verbose_name='Cliente VIP') 
    mayorista = models.BooleanField('Es Mayorista')
    ctacte = models.BooleanField('Cuenta Corriente Habitada')
    subcuenta = models.IntegerField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    creadopor = models.CharField(db_column='CreadoPor', max_length=50)  # Field name made lowercase.
    creadofecha = models.DateTimeField(db_column='CreadoFecha')  # Field name made lowercase.
    modificadopor = models.CharField(db_column='ModificadoPor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modificadofecha = models.DateTimeField(db_column='ModificadoFecha', blank=True, null=True)  # Field name made lowercase.
    borradopor = models.CharField(db_column='BorradoPor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    borradofecha = models.DateTimeField(db_column='BorradoFecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes'
        verbose_name = ('Cliente')
        verbose_name_plural = ('Clientes')
        ordering = ['nombre']

    def __str__(self):
        return self.nombre 
    
class ClientesSaldos(models.Model):
    idcliente = models.IntegerField(models.PROTECT, db_column='idCliente', primary_key=True, editable=False)
    nombre = models.CharField(max_length=50)
    saldo = models.DecimalField('Saldo', max_digits=14, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ClientesSaldos'
        verbose_name = ('Saldos de Clientes')
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre 


class ClientesResumenPendiente(models.Model):
    idsucursal = models.ForeignKey(Sucursal, models.PROTECT, db_column='idSucursal', verbose_name='Sucursal')
    nombre = models.CharField(max_length=30)
    letra = models.CharField(max_length=1)
    numero = models.IntegerField()
    remito = models.IntegerField()
    condicion = models.IntegerField()
    fecha = models.DateField(models.DateField)
    idcliente = models.IntegerField(models.PROTECT, db_column='idCliente', primary_key=True, editable=False)
    idvendedor = models.ForeignKey(Vendedor, models.PROTECT, db_column='idvendedor', verbose_name='Vendedor')
    total = models.DecimalField(max_digits=18, decimal_places=2, db_column='Total')
    entrega = models.DecimalField(max_digits=18, decimal_places=2, db_column='Entrega')
    observacion = models.CharField(max_length=50, db_column='Observacion')
    multcli = models.IntegerField(db_column='MultCli')

    class Meta:
        managed = False
        db_table = 'ClientesResumenPendiente'
        verbose_name = ('Resumen Pendiente')
        ordering = ['fecha']
    
    def __str__(self):
        return self.fecha        


class stockMedidaView(models.Model):
    idlista = models.IntegerField()
    medida = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    stock = models.IntegerField()
    minimo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stockMedidaView'
        verbose_name = ('Stock Actual')
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre 