# -*- coding: utf-8 -*-
#TODO: REFACTOR!!!
#FIXME: Se tiene que insertar el id de la bodega en la anulación
'''
Created on 25/05/2010
@author: Luis Carlos Mejia
'''
from PyQt4.QtCore import pyqtSlot, Qt, QModelIndex, QDate, QString
from PyQt4.QtGui import QTabWidget,QPrintPreviewDialog,QPixmap,QPainter , QPrintDialog,QTextTableFormat, QTextCursor, QFont,QPrinter,QTextCharFormat, QTextFormat, QTextDocument, QTextBlockFormat ,QDataWidgetMapper, QSortFilterProxyModel, QMessageBox, \
    QAbstractItemView, QCompleter, QDialog, qApp, QFormLayout,QFontMetrics, QVBoxLayout, \
    QDateEdit, QDoubleSpinBox, QLabel, QFrame, QDialogButtonBox, QPlainTextEdit, \
    QComboBox, QGridLayout, QIcon
from PyQt4.QtSql import QSqlQuery, QSqlQueryModel, QSqlDatabase
from decimal import Decimal
from facturadelegate import FacturaDelegate, \
    SingleSelectionModel
from facturamodel import FacturaModel
from ui.Ui_tbfactura import Ui_tbFactura
from herramientas import constantes
from herramientas.moneyfmt import moneyfmt
import logging
from ctypes.wintypes import INT
from test.test_getargs2 import Int
from articulos import dlgArticulo
from test.test_iterlen import len
from impresion import frmImpresion





#el modelo de la existencia
IDARTICULOEX, DESCRIPCIONEX, PRECIOEX, COSTOEX, EXISTENCIAEX, \
 IDBODEGAEX = range( 6 )

#controles
IDDOCUMENTO, NDOCIMPRESO, CLIENTE, VENDEDOR, SUBTOTAL, IVA, TOTAL, \
OBSERVACION, FECHA, BODEGA, TASA, TASAIVA, ESTADO, ANULADO, \
ESCONTADO, TOTALFAC, ANULABLE, IDBODEGA = range( 18 )

#table
IDARTICULO, DESCRIPCION, CANTIDAD, PRECIO, TOTALPROD, IDDOCUMENTOT = range( 6 )
#class FrmFactura( QMdiSubWindow, Ui_frmFactura ):


class tbFactura( QTabWidget ,Ui_tbFactura ):
    """
    Implementacion de la interfaz grafica para facturas
    """
    web = "facturas.php?doc="
    DATE_FORMAT = "dd/MM/yyyy"
    def __init__( self ):
        '''
        Constructor
        '''
        super( tbFactura, self ).__init__(  )

# ESTABLECER LA INTERFAZ AL FORMULARIO
        self.setupUi(self)
# VALIDADOR DE MODO DE EDICION
        self.readOnly = True
        self.editmodel = None
#ESTABLECER LA FECHA INICIAL , (establecida al dia de mañana)
        self.categoriesview.headers = ["Descripcion", "Precio", "Unidades","Existencia","","",""]

# Crear el modelo para cargar catalogo de clientes
        self.clientesModel = QSqlQueryModel()
# Crear lista de autocompletado para el combo de clientes
        self.clienteCompleter = QCompleter()     
# Modelo que carga el catalogo de productos
        self.existenciaModel = QSqlQueryModel()

# Establecer todos los controles en modo de edicion
        self.setControls( False )
# Crear la conexion a la base de datos
        self.database = QSqlDatabase.database()

        
        
        self.vistaprevia = False
        
# Cargar los modelos del modo de edicion
        self.updateEditModels()
        self.parent = self.parent()
        

    def newDocument( self ):
        """
        activar todos los controles, llenar los modelos necesarios, 
        crear el modelo FacturaModel, aniadir una linea a la tabla
        """
        self.readOnly = False

        if not self.updateEditModels():
            return

        self.status = False
        self.dtPicker.setDate( self.parentWindow.datosSesion.fecha )

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
            
            self.clientesModel.setQuery( """
                        SELECT idpersona , nombre AS cliente 
                        FROM personas
                        WHERE escliente = 1
                    """)            
            self.cbcliente.setModel( self.clientesModel )
            
            self.cbcliente.setModelColumn( 1 )
            self.clienteCompleter.setCaseSensitivity( Qt.CaseInsensitive )
            self.clienteCompleter.setModel( self.clientesModel )
            self.clienteCompleter.setCompletionColumn( 1 )
            self.cbcliente.setCompleter( self.clienteCompleter )
            


            self.editmodel = FacturaModel( )

                #           Cargar el numero de la factura actual
            query = QSqlQuery( """
                        SELECT MAX(CAST( IFNULL(referencia,0) AS SIGNED)) FROM documentos d WHERE idtipodoc =%d;
                    """ % constantes.IDFACTURA )
            if not query.exec_():
                raise Exception( "No se pudo obtener el numero de la factura" )
            query.first()
            
            if query.size()==0:
                n =1
            else:

                n = str(int(query.value(0)) + 1)
                self.editmodel.printedDocumentNumber = str(int(query.value(0)) + 1)

            self.lblnumero.setText(n)


#            if self.clientesModel.rowCount() == 0:
#                raise UserWarning( "No existen clientes en la"\
#                                          + " base de datos" )
#                return
            
            self.clienteCompleter.setModel(self.clientesModel)
            
            self.cbcliente.setModel(self.clientesModel)
            self.cbcliente.setCompleter(self.clienteCompleter)

#        #Crear el delegado con los articulo y verificar si existen articulos
            self.existenciaModel.setQuery( QSqlQuery( """
            SELECT
                categoria,
                descripcion,
                precio,
                unidadesxcaja,
                -- cajas,
                100 as cajas,
                idprecioproducto
            FROM vw_articulos
             -- WHERE existencia >0
                    """ ) )
            self.categoriesview.update("""
            SELECT
                categoria,
                descripcion,
                precio,
                unidadesxcaja,
                -- cajas,
                100 as cajas,
                idprecioproducto
            FROM vw_articulos
            WHERE idprecioproducto IS NOT NULL
             -- WHERE existencia >0
                    """)
            
            self.categoriesview.expandAll()
            self.categoriesview.setColumnHidden(3,True)
            self.categoriesview.setColumnHidden(4,True)
            
            self.categoriesview.setColumnWidth(0,150)
            self.categoriesview.setColumnWidth(1,60)
            self.categoriesview.setColumnWidth(2,20)
            
            
            
            self.proxyexistenciaModel = SingleSelectionModel()
            self.proxyexistenciaModel.setSourceModel( self.existenciaModel )
#            self.proxyexistenciaModel.setFilterKeyColumn( IDBODEGAEX )

            if self.proxyexistenciaModel.rowCount() == 0:
                raise UserWarning( "No hay articulos en bodega" )

            delegate = FacturaDelegate( self.proxyexistenciaModel )


            self.tabledetails.setItemDelegate( delegate )







            self.tabledetails.setModel( self.editmodel )
            self.tabledetails.setColumnHidden(0,True)
#            self.editmodel.insertRow(1)
            self.editmodel.dataChanged[QModelIndex, QModelIndex].connect( self.updateLabels )

            self.txtobservaciones.setPlainText( "" )
            self.dtPicker.setDate(QDate.currentDate().addDays(1))
            self.editmodel.fecha = QDate.currentDate().addDays(1)
            self.cbcliente.setCurrentIndex( -1 )
            resultado = True
        except UserWarning as inst:
            logging.error( unicode( inst ) )
            QMessageBox.critical( self, qApp.organizationName(), unicode( inst ) )
        finally:
            if self.database.isOpen():
                self.database.close()
        return resultado

    def addActionsToToolBar( self ):
        self.actionRefresh = self.createAction( text = "Actualizar",
                                icon = QIcon.fromTheme( 'view-refresh', QIcon( ":/icons/res/view-refresh.png" ) ),
                                 slot = self.refresh,
                                 shortcut = Qt.Key_F5 )

        self.toolBar.addActions( [
            self.actionNew,
            self.actionRefresh,
            self.actionPreview,
            self.actionPrint,
            self.actionSave,
            self.actionCancel,
        ] )
        self.toolBar.addSeparator()
        self.toolBar.addActions( [
            self.actionGoFirst,
            self.actionGoPrevious,
            self.actionGoLast,
            self.actionGoNext,
            self.actionGoLast
        ] )

    def refresh( self ):
        """
        Actualizar los modelos de edición
        """
        if not self.status:
            if QMessageBox.question( self, qApp.organizationName(),
                                      u"Se perderán todos los cambios en la factura. ¿Esta seguro que desea actualizar?", QMessageBox.Yes | QMessageBox.No ) == QMessageBox.No:
                return
            self.updateEditModels()
        else:
            if self.updateModels():
                QMessageBox.information( None, "Factura",
                                     u"Los datos fueron actualizados con éxito" )


    def printDocument1(self):
        html = u""

        date = QDate.currentDate().toString(self.DATE_FORMAT)
        
        address = Qt.escape("Bario francisco mesa").replace(",","<br>")
        contact = Qt.escape("Luis Mejia")
        balance = 5000
        html += ("<p align=right><img src=':/logo.png'></p>"
                 "<p> align = right>Greasy hands ltd."
                 "<br>New Lombard Street"
                 "<br>London<br>WC13 4PX<br>%s</p>"
                 "<p>%s</p><p>Dear %s, </p>"
                 "<p>The balance of your account is %s.")% (
                   date, address, contact, QString("$ %L1").arg(float(balance),0,"f",2))
                 
        if balance <0 :
            html += ("<p><font color =red><b> Please remit the amount owing immediately.</b></font>")
        else:
            html += "We are delighted to have done business with you."
        
        html += ("</p><p>&nbsp;</p><p>"
                "<table border=1 cellpadding=2 cellspacing=2><tr><td colspan=3>Transaction</td></tr>")
        transactions = [
                        (QDate.currentDate(),500),
                        (QDate.currentDate(),500),
                        (QDate.currentDate(),-500),
                        (QDate.currentDate(),500)
                        ]
        for date, amount in transactions:
            color, status = "black", "Credit"
            if amount <0:
                color, status = "red", "Debid"
            
            html += ("<tr>"
                        "<td align= right>%s</td>"
                        "<td>%s</td><td align=right><font color=%s>%s</font></td></tr>" % (
                        date.toString(self.DATE_FORMAT), status,color, QString("$ %L1").arg(float(abs(amount)), 0, "f",2)))
            
        html += ("</table></p><p style='page-break-after=always;'>"
                 "We hope to continue doing business with you</p>")
                 
        
        pdialog = QPrintDialog() 
        if pdialog.exec_() == QDialog.Accepted:
            printer = pdialog.printer()
            document = QTextDocument()
            document.setHtml(html)
            document.print_(printer)

    def printDocument2(self):
        dialog = QPrintDialog()
        if not dialog.exec_():
            return
        self.printer = dialog.printer()
        headFormat = QTextBlockFormat()
        headFormat.setAlignment(Qt.AlignLeft)
        headFormat.setTextIndent(
            self.printer.pageRect().width()-216)
        bodyFormat = QTextBlockFormat()
        bodyFormat.setAlignment(Qt.AlignJustify)
        lastParaBodyFormat = QTextBlockFormat(bodyFormat)
        lastParaBodyFormat.setPageBreakPolicy(QTextFormat.PageBreak_AlwaysAfter)
        rightBodyFormat = QTextBlockFormat()
        rightBodyFormat.setAlignment(Qt.AlignRight)
        headCharFormat = QTextCharFormat()
        headCharFormat.setFont(QFont("Helvetica",10))
        bodyCharFormat = QTextCharFormat()
        bodyCharFormat.setFont(QFont("Times",11))
        redBodyCharFormat = QTextCharFormat(bodyCharFormat)
        redBodyCharFormat.setForeground(Qt.red)
        tableFormat = QTextTableFormat()
        tableFormat.setBorder(1)
        tableFormat.setCellPadding(2)
        
        document = QTextDocument()
        cursor = QTextCursor(document)
        mainFrame = cursor.currentFrame()
        page = 1
        
        cursor.insertBlock(headFormat, headCharFormat)
        
        for text in ("Greasy Hands Ltd.", "New Lombard Street","London" , "WC13", QDate.currentDate().toString(self.DATE_FORMAT)):
            cursor.insertBlock(headFormat,headCharFormat)
            cursor.insertText(text)
        
        cursor.insertBlock(bodyFormat,bodyCharFormat)
        cursor.insertText("Barrio Francisco Meza")
        
        
        cursor.insertBlock(bodyFormat)
        cursor.insertBlock(bodyFormat,bodyCharFormat)
        cursor.insertText("Dear Lyuis")
        cursor.insertBlock(bodyFormat)
        cursor.insertBlock(bodyFormat,bodyCharFormat)
        cursor.insertText(QString("The balance of your account is $ %L1.").arg(float(500.987),0,"f",2))
        
        cursor.insertBlock(bodyFormat,redBodyCharFormat)
        cursor.insertText("Please remit the amount")
        
        cursor.insertBlock(bodyFormat,bodyCharFormat)
        cursor.insertText("Transaction")

        transactions = [
                        (QDate.currentDate(),500),
                        (QDate.currentDate(),500),
                        (QDate.currentDate(),-500),
                        (QDate.currentDate(),500)
                        ]
        
        
        table = cursor.insertTable(len(transactions), 3, tableFormat)
        
        row = 0
        for date, amount in transactions:
            cellCursor = table.cellAt(row,0).firstCursorPosition()
            cellCursor.setBlockFormat(rightBodyFormat)
            cellCursor.insertText(date.toString(self.DATE_FORMAT),bodyCharFormat)
            
            cellCursor = table.cellAt(row,1).firstCursorPosition()
            cellCursor.insertText("Credit",bodyCharFormat)
            
            cellCursor = table.cellAt(row,2).firstCursorPosition()
            cellCursor.setBlockFormat(rightBodyFormat)
            
            cellCursor.insertText(QString("The balance of your account is $ %L1.").arg(float(amount),0,"f",2),redBodyCharFormat)
            
            row += 1
            
        cursor.setPosition(mainFrame.lastPosition())
        cursor.insertBlock(bodyFormat,bodyCharFormat)
        cursor.insertText("We hope")
        document.print_(self.printer)



    def printDocument(self):
        dialog = QPrintDialog()
        if not dialog.exec_():
            return
        self.printer = dialog.printer()    
        self.imprimir(self.printer)
        self.document.load(self.editmodel)
        

    def preview(self):    
        self.vistaprevia = True     
        preview = frmImpresion(self)
        preview.exec_()
        
           
    def save( self ):
        """
        Guardar el documento actual
        @rtype: bool
        """
        result = False
        try:
            if not self.valid:
                return False

            if QMessageBox.question( self, qApp.organizationName(),
                                     u"¿Esta seguro que desea guardar la factura?",
                                     QMessageBox.Yes | QMessageBox.No ) == QMessageBox.Yes:

                if not self.database.isOpen():
                    if not self.database.open():
                        raise UserWarning( u"No se pudo conectar con la base de datos" )

                self.editmodel.observaciones = self.txtobservaciones.toPlainText()
                if not self.editmodel.save():
                    raise UserWarning( "No se ha podido guardar la factura" )

                QMessageBox.information( None,
                     qApp.organizationName() ,
                     u"""El documento se ha guardado con éxito""" )

                
                self.readOnly = True
                
                self.updateModels()

#                self.navigate( 'last' )
#                self.status = True
                result = True
        except UserWarning as inst:
            logging.error( unicode( inst ) )
            QMessageBox.critical( self, qApp.organizationName(), unicode( inst ) )
        except Exception as inst:
            logging.critical( unicode( inst ) )
            QMessageBox.critical( self, qApp.organizationName(),
                                 u"Hubo un error al guardar la factura" )
        finally:
            if self.database.isOpen():
                self.database.close()
        return result

#    @pyqtSlot(QModelIndex)    
#    def on_categoriesview_doubleClicked(self,index):
    @pyqtSlot(QModelIndex)    
    def on_categoriesview_activated(self,index):
        articulo = self.categoriesview.model().asRecord(index)
        if len(articulo)>0:
            nuevo = True
            
            for i, line in enumerate(self.editmodel.lines):
                if line.itemId == articulo [5]:
                    nuevo = False
                    fila = i
                    line = self.editmodel.lines[self.editmodel.rowCount()-1]
                
            if nuevo:       
                fila = self.editmodel.rowCount()
                self.editmodel.insertRow(fila)
                self.parent.saveAct.setEnabled(True)
                linea = self.editmodel.lines[fila]        
                linea.itemDescription = articulo[0] + " " + articulo [1]
                linea.itemPrice = Decimal(articulo[2])
                linea.itemId = articulo[5]
                
                linea.quantityperbox = int(articulo[3])
            
            
            self.editmodel.lines[fila].quantity += 1
            self.editmodel.lines[fila].existencia  = int(articulo[4]) - self.editmodel.lines[fila].quantity 
            indice =self.editmodel.index( fila,2)
            self.editmodel.dataChanged.emit( indice, indice )
            indice =self.editmodel.index( fila,3)
            self.editmodel.dataChanged.emit( indice, indice )
            indice =self.editmodel.index( fila,5)
            self.editmodel.dataChanged.emit( indice, indice )
    
      
    @pyqtSlot()
    def on_btneditar_clicked( self ):
        articulo = dlgArticulo(self)
        articulo.exec_()
        self.updateEditModels()

    @pyqtSlot( int )   
    def on_cbcliente_currentIndexChanged( self, index ):
        """
        asignar proveedor al objeto self.editmodel
        """
        if self.editmodel is not None:
            numero = self.clientesModel.record( index ).value( "idpersona" )
            self.editmodel.clienteId = int(numero) if numero is not None else 0

    @pyqtSlot( unicode )   
    def on_cbcliente_editTextChanged( self, text ):
        """
        asignar proveedor al objeto self.editmodel
        """
        if self.editmodel is not None:
            self.editmodel.cliente =str( text)


    @pyqtSlot( int )
    
    def on_cbvendedor_currentIndexChanged( self, index ):
        """
        asignar proveedor al objeto self.editmodel
        """
        self.editmodel.vendedorId = self.vendedoresModel.record( index ).value( "idpersona" ).toInt()[0]


    @pyqtSlot( QDate)
    def on_dtPicker_dateChanged( self, date ):
        if self.editmodel is not None:
            self.editmodel.fecha = date

    @pyqtSlot( bool )
    def on_rbcontado_toggled( self, on ):
        """
        Asignar las observaciones al objeto editmodel
        """
        self.editmodel.escontado = 1 if on else 0

    def on_txtSearch_textChanged( self, text ):
        """
        Cambiar el filtro de busqueda
        """
        self.filtermodel.setFilterRegExp( text )

    def setControls( self, status ):
        """
        @param status: false = editando        true = navegando
        """
#        self.actionPrint.setVisible( status )
        self.readOnly = status
        self.txtobservaciones.setReadOnly( status )
#        self.actionPreview.setVisible( status )
#        self.actionAnular.setVisible( status )
#        self.toolBar.setVisible(status)

#        self.lblnfac.setText( self.editmodel.printedDocumentNumber )
        self.swcliente.setCurrentIndex( 0 )
        self.lbltotal.setText( "C$ 0.00" )
        self.tabledetails.setEditTriggers( QAbstractItemView.AllEditTriggers )
#        self.lblanulado.setHidden( True )



        self.tabledetails.horizontalHeader().setStretchLastSection(True)

        self.tabledetails.setColumnHidden( IDARTICULO, True )
        self.tabledetails.setColumnHidden( IDDOCUMENTOT, True )



    def updateLabels( self ):
        self.lbltotal.setText( moneyfmt( self.editmodel.total, 2, "C$ " ) )
        
        

    @property
    def valid( self ):
        """
        Un documento es valido cuando 
        self.printedDocumentNumber != ""
        self.providerId !=0
        self.validLines >0
        self.ivaId !=0
        self.uid != 0
        self.warehouseId != 0
        """
        if int( self.editmodel.clienteId) == 0 and self.editmodel.cliente == "":
            QMessageBox.warning( self, qApp.organizationName(),
                                  "Por favor elija el cliente" )
            self.cbcliente.setFocus()
            
        elif self.editmodel.rowCount() == 0:
            QMessageBox.warning( self, qApp.organizationName(),
                              "Por favor agregue algun articulo a la factura" )
        else:
            return True
        return False


                
    def imprimir(self,printer):
        
        leftMargin = 72
        widthCol = 100

        
        arialFont = QFont("Helvetica",16,3)
        
        fuente =QFontMetrics(arialFont)
        arialLineHeight = fuente.height()
        
        fondo = QPixmap(":/images/res/fondo.png")     
        painter = QPainter(printer)
        pageRect = printer.pageRect()
        page = 1
        
        painter.save()
        if self.vistaprevia:
            painter.drawPixmap(0, 0, 530, 830, fondo)
        
        painter.setFont(arialFont)
        
        y = 180
        x = 35
        painter.drawText(x,y,self.editmodel.fecha.toString("dd   MM   yy"))
        
        y = 210
        x = 85
        
        painter.drawText(x,y, self.editmodel.cliente)
        
        painter.setFont(arialFont)

        
        cajasFont = QFont("Helvetica",10,2)
        x = -5
        y = 295
         
        painter.setFont(cajasFont)
        painter.drawText(x,y - arialLineHeight - 1,"Cajas")
        
        
        for row in self.editmodel.lines:
            painter.setFont(cajasFont)
            x = 2
            painter.drawText(x,y,row.cantidad())

            painter.setFont(arialFont)
            total = moneyfmt(row.total,2,"")
            x = 470 - fuente.width(total)
            painter.drawText(x,y,total)
            
            x =310
            painter.drawText(x,y,moneyfmt(row.itemPrice,2,""))
            


            x = 30                                
            painter.drawText(x,y,row.unidades())
            
            
            x = 80
            painter.drawText(x,y,row.itemDescription)            

            
            
            y+= arialLineHeight
            
        
        total = moneyfmt(self.editmodel.total,2,"")
        y= 690
        x = 470 - fuente.width(total)   
        painter.drawText(x,y,total)
        
        
        painter.setPen(Qt.black)
#        printer.newPage()
        painter.restore()
