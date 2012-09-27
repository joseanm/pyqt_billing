#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 16/04/2011
@author: Luis Carlos Mejia
'''
from interfaz.Ui_dlgpersona import Ui_dlgPersona
from PyQt4.QtGui import QDialog, QDialog,QSortFilterProxyModel,QMessageBox,QAbstractItemView,QCompleter
from PyQt4.QtSql import QSqlTableModel, QSqlDatabase,QSqlQueryModel,QSqlQuery
from PyQt4.QtCore import pyqtSlot, Qt, QTimer, QSize, QRegExp, QVariant
from modelos.personamodel import PersonaModel
from modelos.database import mydb
from pais import DlgPais
 
   
class dlgPersona( QDialog, Ui_dlgPersona ):
        
    def __init__( self ,tipopersona, parent ):
        '''
        Constructor
        '''
        super( dlgPersona, self ).__init__( parent )
        self.setupUi(self)

#        self.tableview.addActions( ( self.actionEdit, self.actionNew ) )
        self.idtipopersona = tipopersona
        self.table = ""
        self.backmodel = QSqlQueryModel()
        self.database = parent.database

        self.filtermodel = QSortFilterProxyModel( self )
        self.filtermodel.setSourceModel( self.backmodel )
        self.filtermodel.setDynamicSortFilter( True )
        self.filtermodel.setFilterKeyColumn( -1 )
        self.filtermodel.setFilterCaseSensitivity( Qt.CaseInsensitive )
        
        self.paisesModel = QSqlQueryModel()
        self.cbpais.setModel( self.paisesModel )
        self.cbpais.setCurrentIndex( -1 )
        self.cbpais.setFocus()
        self.cbpais.setModelColumn( 1 )
        self.paisescompleter = QCompleter()
        self.paisescompleter.setCaseSensitivity( Qt.CaseInsensitive )
        self.paisescompleter.setModel( self.paisesModel )
        self.paisescompleter.setCompletionColumn( 1 )
        self.cbpais.setCompleter( self.paisescompleter )      


        self.proveedoresModel = QSqlQueryModel()
        self.cbproveedor.setModel( self.proveedoresModel )
        self.cbproveedor.setCurrentIndex( -1 )
        self.cbproveedor.setFocus()
        self.cbproveedor.setModelColumn( 1 )
        self.proveedorcompleter = QCompleter()
        self.proveedorcompleter.setCaseSensitivity( Qt.CaseInsensitive )
        self.proveedorcompleter.setModel( self.proveedoresModel )
        self.proveedorcompleter.setCompletionColumn( 1 )
        self.cbproveedor.setCompleter( self.proveedorcompleter ) 


#        self.tableview.setModel(self.filtermodel)
        self.cbsexo.setCurrentIndex(-1)
        self.txtnombre.setFocus()
        self.setReadOnly(True)
        QTimer.singleShot( 0, self.updateModels )
       
    @pyqtSlot( "QString" )
    def on_txtSearch_textChanged( self, text ):
        """
        Cambiar el filtro de busqueda
        """
        self.filtermodel.setFilterRegExp( text )
       
    def setReadOnly(self,status):
        self.txtSearch.setText("")
        self.txtnombre.setText("")
        self.txtempresa.setText("")
        self.txttelefono.setText("")
        self.txtcorreo.setText("")
        self.cbpais.setCurrentIndex(-1)
        self.txtnombre.setFocus()
        if status:
            self.editmodel = None
            self.swpanel.setCurrentIndex(0)
        else:
            
            self.editmodel = PersonaModel(self.database,self.idtipopersona)
            self.swpanel.setCurrentIndex(1)
            

#
#        if status:
#            self.tableview.setEditTriggers( QAbstractItemView.AllEditTriggers )
##            self.tableview.edit( self.tableview.selectionModel().currentIndex() )
#        else:
#            self.tableview.setEditTriggers( QAbstractItemView.NoEditTriggers )
#
#        self.actionNew.setVisible(  status )
#        self.actionEdit.setVisible(  status )
#        self.actionDelete.setVisible( status )
#        self.actionCancel.setVisible( not status )
#        self.actionSave.setVisible(not  status )
#        self.backmodel.readOnly = status


    def updateModels( self ):
        """
        Actualizar los modelos, despues de toda operacion que cambie la base de datos se tienen que actualizar los modelos
        """

        try:
            if not self.database.isOpen():
                if not self.database.open():
                    raise UserWarning( u"No se pudo conectar con la base de datos" )
            self.backmodel.setQuery("""
            SELECT
                d.idpersona as Id,
                d.Nombre,
                d.Telefono,
                d.Correo,
                p.nombre as Pais
         FROM personas d JOIN paises p ON p.idpais = d.idpais
         WHERE idaccion = %d""" %self.idtipopersona )
            
            self.tableview.setModel( self.filtermodel )
            
            self.tableview.setColumnHidden(0,True)
#            self.tableview.setColumnWidth(0,200)
#            self.tableview.set


            self.paisesModel.setQuery( """
            SELECT idpais , nombre  
            FROM paises  """  )
            
            if self.paisesModel.rowCount() == 0:
                raise UserWarning( "No existen paises en la"\
                              + " base de datos" )
            self.cbpais.setModel( self.paisesModel )
            self.cbpais.setCurrentIndex( -1 )
            self.cbpais.setModelColumn( 1 )

            self.paisescompleter.setCaseSensitivity( Qt.CaseInsensitive )
            self.paisescompleter.setModel( self.paisesModel )
            self.paisescompleter.setCompletionColumn( 1 )
            self.cbpais.setCompleter( self.paisescompleter )
            
            self.proveedoresModel.setQuery( """
            SELECT 
            idproveedor, nombre 
            FROM proveedores p where p.idproveedor not in (select origen from proveedores where origen is not null);""" )
            
            if self.proveedoresModel.rowCount() == 0:
                raise UserWarning( "No existen proveedores en la"\
                              + " base de datos" )
            self.cbproveedor.setModel( self.proveedoresModel )
            self.cbproveedor.setCurrentIndex( -1 )
            self.cbproveedor.setFocus()
            self.cbproveedor.setModelColumn( 1 )

            self.proveedorcompleter.setCaseSensitivity( Qt.CaseInsensitive )
            self.proveedorcompleter.setModel( self.proveedoresModel )
            self.proveedorcompleter.setCompletionColumn( 1 )
            self.cbproveedor.setCompleter( self.proveedorcompleter )
            self.cbproveedor.setModel( self.proveedoresModel )
            self.cbproveedor.setCurrentIndex(-1)            
            self.database.close()
        except Exception as inst:
            print( unicode( inst ) )
            return False
        finally:
            if self.database.isOpen():
                self.database.close()
        return True
 
 
    @pyqtSlot()
    def on_btnadd_clicked(self):
        self.setReadOnly(False)
        
    @pyqtSlot()
    def on_btnagregar_pais_clicked(self):
        paisdialog = DlgPais(self)
        paisdialog.exec_()
        self.updateModels()
        
    @pyqtSlot()
    def on_btncancelar_clicked(self):
        self.setReadOnly(True)
  
    @pyqtSlot( int )
    def on_cbproveedor_currentIndexChanged( self, index ):
        """
        asignar la concepto al objeto self.editmodel
        """
        if self.editmodel is not None:
            self.editmodel.idproveedor = self.proveedoresModel.record( index ).value( "idproveedor" ).toInt()[0]
    
    @pyqtSlot( int )
    def on_cbpais_currentIndexChanged( self, index ):
        """
        asignar la concepto al objeto self.editmodel
        """
        if self.editmodel is not None:
            self.editmodel.idpais = self.paisesModel.record( index ).value( "idpais" ).toInt()[0]
        
    @pyqtSlot()
    def on_btnguardar_clicked(self): 
        self.editmodel.nombre = self.txtnombre.text()
        self.editmodel.telefono = self.txttelefono.text()
        self.editmodel.correo = self.txtcorreo.text()
        self.editmodel.empresa = self.txtempresa.text()
        self.editmodel.eshombre = self.cbsexo.currentIndex()
        self.editmodel.descuento = self.txtdescuento.value()
        
        if self.editmodel.valid():
            if self.editmodel.save():
                QMessageBox.information(None,"Guardar", self.editmodel.mensaje)
                self.setReadOnly(True)
                self.updateModels()
            else:
                QMessageBox.critical(None,"Guardar", self.editmodel.mensaje)
        else:
            QMessageBox.critical(None,"Guardar", self.editmodel.mensaje)    
            
    @pyqtSlot( int )
    def on_cbproveedor_currentIndexChanged( self, index ):
        """
        asignar la concepto al objeto self.editmodel
        """
        if self.editmodel is not None:
            self.editmodel.idproveedor = self.proveedoresModel.record( index ).value( "idproveedor" ).toInt()[0]
