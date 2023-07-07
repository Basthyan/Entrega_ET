from django.db import models

# Create your models here.
class tipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(
        primary_key=True, db_column='idTipo', verbose_name='ID_tipo_Usuario')
    tipoUsuario = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.tipoUsuario)


class Usuario(models.Model):
    # rut - Nombre - AppPaterno - appMaterno - fecha Nacimiento
    # tipo - correo - telefono - activo
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    appPaterno = models.CharField(max_length=30, blank=False, null=False)
    appMaterno = models.CharField(max_length=30, blank=False, null=False)
    fechaNacimiento = models.DateField(blank=False, null=False)
    tipoUsuario = models.ForeignKey(
        'tipoUsuario', on_delete=models.CASCADE, db_column='idTipo')
    correo = models.EmailField(
        unique=True, blank=False, null=False, max_length=100)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    activo = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.appPaterno)+" "+str(self.appMaterno)
    
class despacho(models.Model):
    #correo-nombre-apellidos-rut-direccion-numero-dpto/casa-fechaEntrega
    correo = models.EmailField(
        unique=True, blank=False, null=False, max_length=100)
    nombres = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=60, blank=False, null=False)
    rut = models.CharField(max_length=10, primary_key=True)
    direccion = models.CharField(max_length=100, blank=False, null=False)
    numero = models.CharField(max_length=10, blank=False, null=False)
    dpto = models.CharField(max_length=15, blank=False, null=False)
    fechaEntrega = models.DateField(blank=False, null=False)
    ID_despacho = models.CharField(max_length=10, blank=False, null=False)
    telefono = models.IntegerField(max_length=13)

class producto(models.Model):
    #nombre - decripcion - precio - cantidad - ID
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.CharField(max_length=500, blank=False, null=False)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    ID = models.CharField(max_length=10, primary_key=True)

class pedido(models.Model):
    #ID_pedido - producto - cantidad 
    ID_pedido = models.CharField(max_length=10, primary_key=True)
    cantidad = models.IntegerField()