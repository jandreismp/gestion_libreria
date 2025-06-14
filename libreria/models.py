# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adquisicion(models.Model):
    id_adquisicion = models.AutoField(primary_key=True)
    cant_adqs = models.IntegerField(blank=True, null=True)
    fecha_adqs = models.DateField(blank=True, null=True)
    id_edit = models.ForeignKey('Editorial', models.DO_NOTHING, db_column='id_edit', blank=True, null=True)
    id_empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)
    isbn = models.ForeignKey('Libro', models.DO_NOTHING, db_column='isbn', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adquisicion'


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=30)
    esado = models.CharField(max_length=30)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    tipo = models.TextField()  # This field type is a guess.
    telefono = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'cliente'


class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha = models.DateField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='id_empleado')

    class Meta:
        managed = False
        db_table = 'compra'


class DetalleCompra(models.Model):
    pk = models.CompositePrimaryKey('isbn', 'id_compra')
    isbn = models.ForeignKey('Libro', models.DO_NOTHING, db_column='isbn')
    id_compra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='id_compra')
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_compra'


class Editorial(models.Model):
    id_edit = models.AutoField(primary_key=True)
    telefono_conect = models.CharField(max_length=15)
    calle = models.CharField(max_length=50)
    estado = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'editorial'


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_supervisor = models.ForeignKey('self', models.DO_NOTHING, db_column='id_supervisor')

    class Meta:
        managed = False
        db_table = 'empleado'


class Gerente(models.Model):
    id_gerente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_edit = models.OneToOneField(Editorial, models.DO_NOTHING, db_column='id_edit', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gerente'


class Libro(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13)
    titulo = models.CharField(max_length=100)
    tema = models.CharField(max_length=30, blank=True, null=True)
    precio = models.FloatField()
    id_edit = models.ForeignKey(Editorial, models.DO_NOTHING, db_column='id_edit')

    class Meta:
        managed = False
        db_table = 'libro'
