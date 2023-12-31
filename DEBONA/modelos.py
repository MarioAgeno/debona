# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Compras(models.Model):
    idcodcom = models.CharField(db_column='idCodCom', max_length=2)  # Field name made lowercase.
    letra = models.CharField(max_length=1)
    numero = models.DecimalField(max_digits=12, decimal_places=0)
    fecha = models.DateField()
    fecharegistro = models.DateField(db_column='fechaRegistro')  # Field name made lowercase.
    idproveedor = models.IntegerField(db_column='idProveedor')  # Field name made lowercase.
    gravado = models.DecimalField(max_digits=12, decimal_places=2)
    nogravado = models.DecimalField(max_digits=12, decimal_places=2)
    exento = models.DecimalField(max_digits=12, decimal_places=2)
    iva = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    entrega = models.DecimalField(max_digits=12, decimal_places=2)
    fechapago = models.DateField(db_column='fechaPago', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=1)
    observacion = models.CharField(max_length=50)
    operador = models.CharField(max_length=128)
    idsucursal = models.IntegerField(db_column='idSucursal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Compras'


class Comprasdetalle(models.Model):
    idcompras = models.IntegerField(db_column='idCompras')  # Field name made lowercase.
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ComprasDetalle'



class Menu(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    texto = models.CharField(db_column='Texto', max_length=50)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idmenusuperior = models.ForeignKey('self', models.DO_NOTHING, db_column='IdMenuSuperior', blank=True, null=True)  # Field name made lowercase.
    grupo = models.SmallIntegerField(db_column='Grupo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Menu'


class Menuusuariosperfiles(models.Model):
    idmenu = models.OneToOneField(Menu, models.DO_NOTHING, db_column='IdMenu', primary_key=True)  # Field name made lowercase. The composite primary key (IdMenu, IdUsuarioPerfil) found, that is not supported. The first column is selected.
    idusuarioperfil = models.ForeignKey('Usuariosperfil', models.DO_NOTHING, db_column='IdUsuarioPerfil')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MenuUsuariosPerfiles'
        unique_together = (('idmenu', 'idusuarioperfil'),)


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    idlocalidad = models.CharField(db_column='idLocalidad', max_length=5)  # Field name made lowercase.
    idtipopersona = models.IntegerField(db_column='idTipoPersona')  # Field name made lowercase.
    idcodiva = models.CharField(db_column='idCodIVA', max_length=3)  # Field name made lowercase.
    cuit = models.DecimalField(db_column='CUIT', max_digits=11, decimal_places=0)  # Field name made lowercase.
    ingbrutos = models.CharField(db_column='ingBrutos', max_length=15)  # Field name made lowercase.
    telefono = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    email = models.CharField(db_column='eMail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    observacion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Proveedor'




class Aliciva(models.Model):
    codafip = models.IntegerField(db_column='codAFIP', primary_key=True)  # Field name made lowercase.
    alicuota = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'alicIVA'


class Audtablas(models.Model):
    tipo = models.CharField(max_length=1)
    tabla = models.CharField(max_length=50)
    idtabla = models.IntegerField(db_column='idTabla')  # Field name made lowercase.
    usuario = models.CharField(max_length=50)
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'audTablas'



class Caja(models.Model):
    caja = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    idusuario = models.CharField(db_column='idUsuario', max_length=128)  # Field name made lowercase.
    sucursal = models.IntegerField()
    saldoinicio = models.DecimalField(db_column='saldoInicio', max_digits=14, decimal_places=2)  # Field name made lowercase.
    ingresos = models.DecimalField(max_digits=14, decimal_places=2)
    egresos = models.DecimalField(max_digits=14, decimal_places=2)
    saldo = models.DecimalField(max_digits=14, decimal_places=2)
    recuento = models.DecimalField(max_digits=14, decimal_places=2)
    fechacierre = models.DateTimeField(blank=True, null=True)
    observacion = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'caja'


class Cajaarqueo(models.Model):
    idcaja = models.IntegerField(db_column='idCaja')  # Field name made lowercase.
    cantidad = models.IntegerField()
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    detalle = models.CharField(max_length=20)
    importe = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cajaArqueo'


class Cajadetalle(models.Model):
    idcaja = models.IntegerField(db_column='idCaja')  # Field name made lowercase.
    idventas = models.IntegerField(db_column='idVentas')  # Field name made lowercase.
    importe = models.DecimalField(max_digits=12, decimal_places=2)
    observacion = models.BinaryField()
    mediopago = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cajaDetalle'


class Clientesna(models.Model):
    cuit = models.DecimalField(db_column='CUIT', primary_key=True, max_digits=11, decimal_places=0)  # Field name made lowercase.
    motivo = models.CharField(db_column='MOTIVO', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientesNA'


class Codcomision(models.Model):
    id = models.IntegerField(primary_key=True)
    comision = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'codComision'


class Codcom(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    nombre = models.CharField(max_length=30)
    multcom = models.SmallIntegerField(db_column='multCom')  # Field name made lowercase.
    multpro = models.SmallIntegerField(db_column='multPro')  # Field name made lowercase.
    multsto = models.SmallIntegerField(db_column='multSto')  # Field name made lowercase.
    letra = models.CharField(max_length=1)
    libroiva = models.BooleanField(db_column='libroIVA')  # Field name made lowercase.
    numero = models.DecimalField(db_column='Numero', max_digits=12, decimal_places=0)  # Field name made lowercase.
    copias = models.IntegerField()
    codafip = models.CharField(db_column='codAFIP', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'codcom'


class Formaspagos(models.Model):
    nombre = models.CharField(max_length=50)
    condicion = models.SmallIntegerField()
    plazo = models.SmallIntegerField()
    cuotas = models.SmallIntegerField()
    entregacuota1 = models.BooleanField()
    interes = models.DecimalField(max_digits=6, decimal_places=2)
    paridad = models.DecimalField(max_digits=12, decimal_places=2)
    formulario = models.CharField(max_length=50)
    idmediospagos = models.ForeignKey('Mediospagos', models.DO_NOTHING, db_column='idMediosPagos')  # Field name made lowercase.
    idmoneda = models.ForeignKey('Monedas', models.DO_NOTHING, db_column='idMoneda')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formaspagos'



class Mediospagos(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mediospagos'


class Menutree(models.Model):
    sec_codacce = models.CharField(primary_key=True, max_length=10)
    sec_descacce = models.CharField(max_length=20)
    sec_promptacc = models.CharField(max_length=40)
    sec_nivelacce = models.SmallIntegerField()
    sec_tipoacce = models.SmallIntegerField()
    sec_doacce = models.CharField(max_length=50)
    sec_keyacce = models.CharField(max_length=10, blank=True, null=True)
    sec_condacce = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menuTree'


class Menutreeperfil(models.Model):
    sec_codacce = models.CharField(max_length=10)
    idperfil = models.IntegerField(db_column='idPerfil')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menuTreePerfil'
        unique_together = (('idperfil', 'sec_codacce'),)



class Numeros(models.Model):
    idsucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='idSucursal')  # Field name made lowercase.
    codafip = models.CharField(db_column='codAFIP', max_length=3)  # Field name made lowercase.
    puntoventa = models.IntegerField()
    numero = models.IntegerField()
    renglones = models.SmallIntegerField()
    copias = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'numeros'


class Recibos(models.Model):
    idventa = models.IntegerField(db_column='idVenta')  # Field name made lowercase.
    recibo = models.BigIntegerField()
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    importecobrado = models.DecimalField(db_column='ImporteCobrado', max_digits=12, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recibos'


class Stockclientes(models.Model):
    idventa = models.IntegerField(db_column='idVenta')  # Field name made lowercase.
    idlista = models.IntegerField(db_column='idLista')  # Field name made lowercase.
    cantidad = models.IntegerField()
    retirado = models.IntegerField()
    fecha = models.DateField(blank=True, null=True)
    numero = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    comentario = models.CharField(db_column='Comentario', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stockClientes'


class Usuarios(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    idperfil = models.ForeignKey('Usuariosperfil', models.DO_NOTHING, db_column='idPerfil')  # Field name made lowercase.
    idsucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='idSucursal')  # Field name made lowercase.
    puntoventa = models.IntegerField()
    idvendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='idVendedor', blank=True, null=True)  # Field name made lowercase.
    nombrecompleto = models.CharField(db_column='NombreCompleto', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    ctrlfiscal = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'usuarios'


class Usuariosperfil(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'usuariosPerfil'


class Validacion(models.Model):
    idsucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='idSucursal')  # Field name made lowercase.
    fecha = models.DateTimeField()
    solicitado = models.CharField(max_length=30)
    comentario = models.CharField(max_length=50, blank=True, null=True)
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.
    idcodven = models.ForeignKey(Codven, models.DO_NOTHING, db_column='idCodVen')  # Field name made lowercase.
    numero = models.DecimalField(max_digits=12, decimal_places=0)
    validacion = models.IntegerField()
    hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validacion'


class Vendedordesc(models.Model):
    idmarca = models.OneToOneField(Marcas, models.DO_NOTHING, db_column='idMarca', primary_key=True)  # Field name made lowercase. The composite primary key (idMarca, idFamilia) found, that is not supported. The first column is selected.
    idfamilia = models.ForeignKey(Familias, models.DO_NOTHING, db_column='idFamilia')  # Field name made lowercase.
    desc1 = models.DecimalField(max_digits=6, decimal_places=2)
    desc2 = models.DecimalField(max_digits=6, decimal_places=2)
    desc3 = models.DecimalField(max_digits=6, decimal_places=2)
    desc4 = models.DecimalField(max_digits=6, decimal_places=2)
    desc5 = models.DecimalField(max_digits=6, decimal_places=2)
    desc6 = models.DecimalField(max_digits=6, decimal_places=2)
    desc7 = models.DecimalField(max_digits=6, decimal_places=2)
    desc8 = models.DecimalField(max_digits=6, decimal_places=2)
    desc9 = models.DecimalField(max_digits=6, decimal_places=2)
    desc10 = models.DecimalField(max_digits=6, decimal_places=2)
    desc11 = models.DecimalField(max_digits=6, decimal_places=2)
    desc12 = models.DecimalField(max_digits=6, decimal_places=2)
    desc13 = models.DecimalField(max_digits=6, decimal_places=2)
    desc14 = models.DecimalField(max_digits=6, decimal_places=2)
    desc15 = models.DecimalField(max_digits=6, decimal_places=2)
    desc16 = models.DecimalField(max_digits=6, decimal_places=2)
    desc17 = models.DecimalField(max_digits=6, decimal_places=2)
    desc18 = models.DecimalField(max_digits=6, decimal_places=2)
    desc19 = models.DecimalField(max_digits=6, decimal_places=2)
    desc20 = models.DecimalField(max_digits=6, decimal_places=2)
    desc21 = models.DecimalField(max_digits=6, decimal_places=2)
    desc22 = models.DecimalField(max_digits=6, decimal_places=2)
    desc23 = models.DecimalField(max_digits=6, decimal_places=2)
    desc24 = models.DecimalField(max_digits=6, decimal_places=2)
    desc25 = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'vendedorDesc'
        unique_together = (('idmarca', 'idfamilia'),)


class Ventas(models.Model):
    idsucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, db_column='idSucursal')  # Field name made lowercase.
    idcodven = models.ForeignKey(Codven, models.DO_NOTHING, db_column='idCodVen')  # Field name made lowercase.
    letra = models.CharField(max_length=1)
    numero = models.DecimalField(max_digits=12, decimal_places=0)
    remito = models.DecimalField(max_digits=12, decimal_places=0)
    condicion = models.SmallIntegerField()
    fecha = models.DateField()
    idformapago = models.ForeignKey(Formaspagos, models.DO_NOTHING, db_column='idFormaPago')  # Field name made lowercase.
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.
    idvendedor = models.ForeignKey(Vendedor, models.DO_NOTHING, db_column='idVendedor')  # Field name made lowercase.
    gravado = models.DecimalField(max_digits=12, decimal_places=2)
    exento = models.DecimalField(max_digits=12, decimal_places=2)
    iva = models.DecimalField(db_column='IVA', max_digits=12, decimal_places=2)  # Field name made lowercase.
    percepib = models.DecimalField(db_column='percepIB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=12, decimal_places=2)  # Field name made lowercase.
    entrega = models.DecimalField(db_column='Entrega', max_digits=12, decimal_places=2)  # Field name made lowercase.
    recibo = models.BigIntegerField(blank=True, null=True)
    fechapago = models.DateField(db_column='fechaPago', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=1)
    comision = models.BooleanField()
    codcomision = models.ForeignKey(Codcomision, models.DO_NOTHING, db_column='codComision')  # Field name made lowercase.
    noestadisticas = models.BooleanField(db_column='NoEstadisticas')  # Field name made lowercase.
    stockcliente = models.BooleanField(db_column='stockCliente')  # Field name made lowercase.
    cae = models.BigIntegerField(blank=True, null=True)
    caevto = models.DateField(blank=True, null=True)
    codbarra = models.CharField(max_length=50)
    idusuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    observacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas'


class Ventasdetalle(models.Model):
    idventa = models.ForeignKey(Ventas, models.DO_NOTHING, db_column='idVenta')  # Field name made lowercase.
    idlista = models.IntegerField(db_column='idLista')  # Field name made lowercase.
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    costo = models.DecimalField(max_digits=12, decimal_places=2)
    descuento = models.DecimalField(max_digits=6, decimal_places=2)
    gravado = models.DecimalField(max_digits=12, decimal_places=2)
    exento = models.DecimalField(max_digits=12, decimal_places=2)
    aliciva = models.DecimalField(db_column='AlicIVA', max_digits=6, decimal_places=2)  # Field name made lowercase.
    iva = models.DecimalField(db_column='IVA', max_digits=12, decimal_places=2)  # Field name made lowercase.
    percepib = models.DecimalField(db_column='percepIB', max_digits=12, decimal_places=2)  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=12, decimal_places=2)  # Field name made lowercase.
    reventa = models.CharField(max_length=1)
    idoperario = models.IntegerField(db_column='idOperario', blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ventasDetalle'



