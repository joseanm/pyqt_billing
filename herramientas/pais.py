#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 16/04/2011
@author: Luis Carlos Mejia
'''
from interfaz.Ui_dlgpais import Ui_DlgPais
from PyQt4.QtGui import QMainWindow, QDialog,QSortFilterProxyModel,QMessageBox,QAbstractItemView
from PyQt4.QtSql import QSqlTableModel, QSqlDatabase,QSqlQueryModel,QSqlQuery
from PyQt4.QtCore import pyqtSlot, Qt, QTimer, QSize, QRegExp, QVariant
from modelos.paismodel import PaisModel
from modelos.database import mydb
 
   
class DlgPais( QDialog, Ui_DlgPais ):
        
    def __init__( self ,parent ):
        '''
        Constructor
        '''
        super( DlgPais, self ).__init__( parent )
        self.setupUi(self)

        
        self.table = ""
        self.backmodel = QSqlQueryModel()
        self.database = parent.database

        self.filtermodel = QSortFilterProxyModel( self )
        self.filtermodel.setSourceModel( self.backmodel )
        self.filtermodel.setDynamicSortFilter( True )
        self.filtermodel.setFilterKeyColumn( -1 )
        self.filtermodel.setFilterCaseSensitivity( Qt.CaseInsensitive )

#        self.tableview.setModel(self.filtermodel)

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
        if status:
            self.editmodel = None
            self.swpanel.setCurrentIndex(0)
            self.txtnombre.setText("")
            self.txtcodigo.setText("")
        else:
            
            self.editmodel = PaisModel(self.database)
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
            self.backmodel.setQuery("Select codigoarea as 'Codigo Area' , nombre as Pais from paises")
            
            self.tableview.setModel( self.filtermodel )
#            self.tableview.setColumnHidden(0,True)
#            self.tableview.setColumnWidth(0,200)
#            self.tableview.set
            self.database.close()
        except:
            return False
        finally:
            if self.database.isOpen():
                self.database.close()
        return True
 
 
    @pyqtSlot()
    def on_btnadd_clicked(self):
        self.setReadOnly(False)
        
    @pyqtSlot()
    def on_btncancelar_clicked(self):
        self.setReadOnly(True)
        
    @pyqtSlot()
    def on_btnguardar_clicked(self): 
        self.editmodel.nombre = self.txtnombre.text()
        self.editmodel.codigo = self.txtcodigo.text()
        if self.editmodel.valid():
            if self.editmodel.save():
                QMessageBox.information(None,"Guardar", self.editmodel.mensaje)
                self.setReadOnly(True)
                self.updateModels()
            else:
                QMessageBox.critical(None,"Guardar", self.editmodel.mensaje)
        else:
            QMessageBox.critical(None,"Guardar", self.editmodel.mensaje)    
            
