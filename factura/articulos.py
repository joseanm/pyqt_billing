# -*- coding: utf-8 -*-
'''
Created on 21/08/2011
@author: Luis Carlos Mejia
'''
from PyQt4.QtCore import pyqtSlot, Qt, QModelIndex, QTimer, QDate, QDateTime
from PyQt4.QtGui import QMainWindow,QDataWidgetMapper, QSortFilterProxyModel, QMessageBox, \
    QAbstractItemView, QCompleter, QDialog, qApp, QFormLayout, QVBoxLayout, \
    QDateEdit, QDoubleSpinBox, QLabel, QFrame, QDialogButtonBox, QPlainTextEdit, \
    QComboBox, QGridLayout, QIcon
from PyQt4.QtSql import QSqlQuery, QSqlQueryModel, QSqlDatabase
from decimal import Decimal
from facturadelegate import FacturaDelegate, \
    SingleSelectionModel
from facturamodel import FacturaModel
from ui.Ui_dlgarticulo import Ui_dlgArticulo
from herramientas import constantes
from herramientas.moneyfmt import moneyfmt
import logging
from ctypes.wintypes import INT
from test.test_getargs2 import Int
from test.test_iterlen import len

class dlgArticulo( QDialog, Ui_dlgArticulo ):
    """
    Implementacion de la interfaz grafica para facturas
    """
    web = "facturas.php?doc="
    def __init__( self ,parent ):
        '''
        Constructor
        '''
        super( dlgArticulo, self ).__init__(  )
# ESTABLECER LA INTERFAZ AL FORMULARIO
        self.setupUi(self)
        self.ckprecio.setChecked(False)
        self.ckunit.setChecked(False)
        self.database = QSqlDatabase.database()
        self.categoriesview.headers = ["Descripcion", "Precio Unit.", "Unidades Caja","","","",""]
        self.updateEditModels()

        

    @pyqtSlot(QModelIndex)    
    def on_categoriesview_activated(self,index):
        self.updateLabels(index)

    @pyqtSlot(QModelIndex)    
    def on_categoriesview_clicked(self,index):
        self.updateLabels(index)
        
    def updateLabels(self,index):
        articulo = self.categoriesview.model().asRecord(index)
        if len(articulo)>0:
            self.txtcategoria.setText( articulo[0])
            self.txtmarca.setText( articulo[1])
            
            self.articuloId = articulo[4]
            
            self.precioanterior = Decimal(articulo[2]) 
            self.unidadesanterior = int(articulo[3])
            
            if not self.ckprecio.isChecked(): 
                self.precio = Decimal(articulo[2])
                self.txtprecio.setValue(self.precio)
            
            if not self.ckunit.isChecked():
                self.unidades = int(articulo[3])
                self.txtunidades.setValue(self.unidades)

    @pyqtSlot(float)    
    def on_txtprecio_valueChanged(self,value):
        self.precio = str(value)
        print self.precio    

    @pyqtSlot(int)    
    def on_txtunidades_valueChanged(self,value):
        self.unidades = int(value)
        print self.unidades
        
    @pyqtSlot()
    def on_btncancelar_clicked(self):
        self.close()

    @pyqtSlot()
    def on_btnguardar_clicked(self):
        if self.save():
            QMessageBox.information(None,"Actualizar precios de Articulos","Los cambios han sido guardados")
            self.updateEditModels()
        
        
    def updateEditModels( self ):
        """
        Este metodo actualiza los modelos usados en el modo edición
        """
        resultado = False
        try:
            if not self.database.isOpen():
                if not self.database.open():
                    raise UserWarning( u"No se pudo abrir la conexión "\
                                       + "con la base de datos" )

            
            self.categoriesview.update("""
SELECT 
c.nombre as categoria,
CONCAT(m.nombre , ' ',IFNULL(p.contenido,"")) as marca,
pp.precio,
pp.unidadesxcaja,
p.idproducto
FROM productos p
JOIN marcas m ON m.idmarca = p.idmarca
JOIN categorias c ON c.idcategoria = p.idcategoria
LEFT JOIN preciosproducto pp ON pp.idproducto = p.idproducto AND pp.activo =1
;
             
                    """)
            
            self.categoriesview.expandAll()
            self.categoriesview.setColumnHidden(3,True)
            self.proxyexistenciaModel = SingleSelectionModel()
            self.proxyexistenciaModel.setSourceModel( self.categoriesview.model() )
            resultado = True
        except UserWarning as inst:
            logging.error( unicode( inst ) )
            QMessageBox.critical( self, qApp.organizationName(), unicode( inst ) )
        finally:
            if self.database.isOpen():
                self.database.close()
        return resultado
    
    
    def save(self):
        resultado = False
        try:
            if not self.database.isOpen():
                if not self.database.open():
                    raise UserWarning( u"No se pudo abrir la conexión "\
                                       + "con la base de datos" )
            
            if not self.database.transaction():
                raise Exception( u"No se pudo comenzar la transacción" )
            
                    
                    
            
            query = QSqlQuery()
            

            if not query.prepare( """
            UPDATE preciosproducto 
            SET activo = 0
            WHERE idproducto = :id;
            """ ):
                raise Exception( "No se pudo preparar la consulta para actualizar" )
            query.bindValue( ":id", self.articuloId)
            
            if not query.exec_():
                raise Exception( "No se pudo desactivar el precio actual" )
            
            
            if not query.prepare( """
            INSERT INTO preciosproducto(idproducto,precio,unidadesxcaja)
            VALUES (:id,:precio,:cantidad);
            """ ):
                raise Exception( "No se pudo preparar la consulta para insertar los nuevos precios" )
            query.bindValue( ":id", self.articuloId)
            query.bindValue( ":precio", self.precio)
            query.bindValue( ":unidades", self.unidades )

            if not query.exec_():
                raise Exception( "No se pudo insertar el nuevo precio" )
     
            if not self.database.commit():
                raise Exception( "No se pudo hacer commit" )

            resultado = True
        except UserWarning as inst:
            self.database.rollback()
            print  unicode( inst ) 
            QMessageBox.critical( self, qApp.organizationName(), unicode( inst ) )
            resultado = False
        finally:
            if self.database.isOpen():
                self.database.close()
        return resultado