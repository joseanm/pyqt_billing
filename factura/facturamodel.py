# -*- coding: utf-8 -*-
'''
Created on 18/05/2010

@author: Luis Carlos Mejia Garcia
'''
from PyQt4.QtCore import QAbstractTableModel, QModelIndex, Qt, QDateTime
from PyQt4.QtSql import QSqlDatabase, QSqlQuery
from decimal import Decimal
from lineafactura import LineaFactura
from herramientas import constantes
#from utility.decorators import return_decimal
from herramientas.moneyfmt import moneyfmt
#from utility.movimientos import movFacturaCredito
import logging
#from utility.docbase import DocumentBase
#Los datos de la existencia
IDARTICULOEX, DESCRIPCIONEX, PRECIOEX, COSTOEX, EXISTENCIAEX, \
IDBODEGAEX = range( 6 )

IDARTICULO, DESCRIPCION, CANTIDAD, UNIDADES, PRECIO, TOTALPROD = range( 6 )
class FacturaModel( QAbstractTableModel ):
    """
    esta clase es el modelo utilizado en la tabla en la que se editan 
    los documentos de factura
    """
    __documentType = constantes.IDFACTURA

    def __init__( self ):
        super( FacturaModel, self ).__init__()


        self.dirty = False


        self.clienteId = 0
        """
        @ivar: El id del cliente al que se le esta facturando
        @type: int
        """
        self.cliente = ""
        """
        @ivar: El nombre del cliente
        @type: string
        """
        self.fecha = None
        """
        @ivar: La fecha de la factura
        @type: QDate
        """        
        self.observaciones = ""
        """
        @ivar: Las observaciones del documento
        @type: string
        """
        self.__ivaTasa = Decimal( 0 )
        """
        @ivar: La tasa de IVA en la factura
        @type: Decimal
        """
        self.ivaId = 0
        """
        @ivar: El id del IVA
        @type: int
        """
        self.lines = []
        """
        @ivar: las lineas de la factura
        @type: LineaFactura[]
        """
        self.printedDocumentNumber = ""

        self.escontado = 1

        self.database = QSqlDatabase.database()

        self.__fechaTope = None
        """
        @ivar: Si la factura es de credito aca se almacena la fecha tope
        @type: QDate
        """
        self.multa = Decimal( 0 )
        """
        @ivar: Si la factura es de credito esta sera la multa que se aplique en 
            caso de mora
        @type: Decimal
        """

    def _setFechaTope( self, value ):
        if value < self.datosSesion.fecha:
            raise ValueError( u"value debe ser mayor que la fecha de la sesión" )

        self.__fechaTope = value
    def _getFechaTope( self ):
        return self.__fechaTope
    fechaTope = property( _getFechaTope, _setFechaTope )


    def removeRows( self, position, rows = 1, _index = QModelIndex() ):

        if self.rowCount() > 0 and self.rowCount() > position:
            self.beginRemoveRows( QModelIndex(), position, position + rows - 1 )
            n = position + rows - 1
# borrar el rango de lineas indicado de la ascendente para que no halla problema con el indice de las lineas 
# muestro la fila de la tabla facturas que esta relacionada a la linea que borre
            while n >= position:
                del self.lines[n]
                n = n - 1

            self.endRemoveRows()
            self.dirty = True
#            if self.rowCount() < 1:
#                self.insertRow( 0 )
            return True
        else:
            return False

    @property
    def total( self ):
        """
        El subtotal del documento, esto es el total antes de aplicarse el IVA
        @rtype: Decimal
        """
        return Decimal(sum( [linea.total for linea in self.lines if linea.valid] ))

    @property
    def costototal( self ):
        return sum( [linea.costototal for linea in self.lines if linea.valid] )

#    @property
#    def total( self ):
#        """
#        El total neto del documento, despues de haber aplicado IVA
#        @rtype: Decimal
#        """
#        return self.subtotal + self.IVA

#    @property
#    def IVA( self ):
#        """
#        El IVA total del documento, se calcula en base a subtotal y rateIVA
#        @rtype: Decimal
#        """
#        return  self.subtotal * ( self.ivaTasa / Decimal( 100 ) )

    def _set_iva_tasa( self, value ):
        self.__ivaTasa = value
    def _get_iva_tasa( self ):
        return self.__ivaTasa if self.applyIva else Decimal( 0 )

    ivaTasa = property( _get_iva_tasa, _set_iva_tasa )

    @property
    def applyIva( self ):
        """
        Si se debe o no aplicar IVA a esta factura, esto es un metodo distinto
        para que sea más facil actualizarlo si la regla de negocio cambia
        """
        return self.bodegaId == 1


    #Clases especificas del modelo
    def rowCount( self, _index = QModelIndex() ):
        return len( self.lines )

    def columnCount( self, _index = QModelIndex() ):
        return 6

    def data( self, index, role = Qt.DisplayRole ):
        """
        darle formato a los campos de la tabla
        """
        if not index.isValid() or not ( 0 <= index.row() < len( self.lines ) ):
            return ""
        line = self.lines[index.row()]
        column = index.column()
        if role == Qt.DisplayRole:
            if column == IDARTICULO:
                return line.itemId
#            Esto es lo que se muestra en la tabla
            elif column == DESCRIPCION:
                return line.itemDescription
            elif column == CANTIDAD:
                return line.quantity if line.quantity != 0 else ""
            elif column == UNIDADES:
                return line.units if line.units != 0 else ""
            elif column == PRECIO:
                return moneyfmt( line.itemPrice , 4, "C$" ) if line.itemPrice != 0 else ""
            elif column == TOTALPROD:
                return moneyfmt( line.total , 4, "C$" ) if line.itemId != 0 else ""
        elif role == Qt.EditRole:
            if column == PRECIO:
                return line.itemPrice
        elif role == Qt.TextAlignmentRole:
#            if column==:
#                return Qt.AlignHCenter | Qt.AlignVCenter
            if column in ( CANTIDAD, UNIDADES, PRECIO, TOTALPROD ):
                return Qt.AlignRight | Qt.AlignVCenter
        elif role == Qt.ToolTipRole:
            if column == CANTIDAD:
                return u"Máximo %d" % line.existencia

    def flags( self, index ):
        if not index.isValid():
            return Qt.ItemIsEnabled
        if index.column() == CANTIDAD:
            return Qt.ItemFlags( QAbstractTableModel.flags( self, index )
                             | Qt.ItemIsEditable )
        else:
            return Qt.ItemFlags( Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def setData( self, index, value, _role = Qt.EditRole ):
        """
        modificar los datos del modelo, este metodo se comunica con el delegate
        """
        if index.isValid() and 0 <= index.row() < len( self.lines ) :
            line = self.lines[index.row()]
            column = index.column()
            if column in ( IDARTICULO, DESCRIPCION ):
                line.itemId = value[IDARTICULOEX]
                line.itemDescription = value[DESCRIPCIONEX]
                line.sugerido = Decimal( value[PRECIOEX] )
                line.itemPrice = Decimal( line.sugerido )
                line.costo = Decimal( value[COSTOEX] )
                line.existencia = value[EXISTENCIAEX]
                if line.existencia < line.quantity :
                    line.quantity = line.existencia
                line.idbodega = int( value[IDBODEGAEX] )

            elif column == CANTIDAD:
                line.quantity = value
                if value == 0:
                    self.removeRow(index.row())
                    
            elif column == PRECIO:
                line.itemPrice = Decimal( value.toString() )

            self.dirty = True


            self.dataChanged.emit( index, index )
            #si la linea es valida y es la ultima entonces aniadir una nueva
#            if  index.row() == len( self.lines ) - 1 and line.valid:
#                self.insertRows( len( self.lines ) )

            return True
        return False

    def insertRows( self, position, rows = 1, _index = QModelIndex() ):
        self.beginInsertRows( QModelIndex(), position, position + rows - 1 )
        for row in range( rows ):
            self.lines.insert( position + row, LineaFactura( self ) )
        self.endInsertRows()
        self.dirty = True
        return True


    def headerData( self, section, orientation, role = Qt.DisplayRole ):
        if role == Qt.TextAlignmentRole:
            if orientation == Qt.Horizontal:
                return Qt.AlignLeft | Qt.AlignVCenter
            return Qt.AlignRight | Qt.AlignVCenter
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            if  section == DESCRIPCION:
                return u"Descripción"
            elif section == UNIDADES:
                return "Unidades"
            elif section == PRECIO:
                return "Precio Unit."
            elif section == TOTALPROD:
                return "Total"
            elif section == CANTIDAD:
                return "Cajas"
        return int( section + 1 )

    @property
    def validLines( self ):
        return len( [line for line in self.lines if line.valid] )

    @property
    def valid( self ):
        try:
            if self.cliente =="":
                raise UserWarning( "Por favor escriba el nombre del cliente" )
            if not self.validLines > 0:
                raise UserWarning( "Existe una linea no valida" )
            if not self.total > 0:
                raise UserWarning( "El total no puede ser 0" )

 
            return True
        except UserWarning as inst:
            self._valid_error = unicode( inst )
            return False

        return True
    def save( self  ):
        """
        Este metodo guarda la factura en la base de datos
        """

        if not self.valid:
                raise Exception( u"Se intento guardar una factura no valida " )


        query = QSqlQuery()
        try:

            if not self.database.transaction():
                raise Exception( u"No se pudo comenzar la transacción" )
            


            if self.clienteId == 0:
                if not query.prepare( """
                INSERT INTO personas (nombre,escliente) 
                VALUES ( :nombre,1)
                """ ):
                    raise Exception( "No se pudo guardar el documento" )
                
                query.bindValue( ":nombre",self.cliente)
            
    
                if not query.exec_():
                    raise Exception( "No se pudo insertar el cliente" )
                
                
                self.clienteId = str(query.lastInsertId())       
                print "id cliente " + self.clienteId   

            if not query.prepare( """
            INSERT INTO documentos (fechacreado,fecha,idtipodoc,
            observaciones,total,idpersona,referencia) 
            VALUES ( NULL,:fecha,:idtipodoc,:observacion,
            :total,:idpersona,:ref)
            """ ):
                raise Exception( "No se pudo guardar el documento" )
            query.bindValue( ":fecha",self.fecha.toString( 'yyyyMMdd' ))
            query.bindValue( ":idtipodoc", self.__documentType )
            query.bindValue( ":observacion", self.observaciones )
            query.bindValue( ":total", self.total.to_eng_string() )
            query.bindValue( ":idpersona", self.clienteId )
            query.bindValue( ":ref", self.printedDocumentNumber )
            
            if not query.exec_():
                raise Exception( "No se pudo insertar el documento" )

            
            inserted_id = str(query.lastInsertId())
            for i, linea in enumerate( [line for line in self.lines if line.valid] ):
                linea.save( inserted_id, i)

            if not self.database.commit():
                raise Exception( "No se pudo guardar la factura" )
            
            return True
        except Exception as inst:
            logging.critical( query.lastError().text() )
            logging.critical( unicode( inst ) )
            self.database.rollback()
            return False
        return True
