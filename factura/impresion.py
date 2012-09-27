#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 29/08/2011

@author: Luis Carlos Mejia
'''
from PyQt4.QtGui import  QPrinter, QPrintPreviewDialog,QFont,QFontMetrics, QPainter, \
QMessageBox, QProgressBar, QPrintPreviewWidget, qApp
from PyQt4.QtWebKit import QWebView
from PyQt4.QtCore import  QUrl, Qt

from herramientas.moneyfmt import moneyfmt



class frmImpresion( QPrintPreviewDialog ):
    """
    Este es un formulario generico que muestra los reportes web generados para las 
    """
    def __init__( self,padre, parent = None ):
        super( frmImpresion, self ).__init__(parent )
        
        self.setWindowFlags( self.windowFlags() | Qt.WindowMaximizeButtonHint )
        
        self.loaded = False
        self.padre = padre
        self.paintRequested[QPrinter].connect( self.reprint )
        
        
#        self.loadFinished[bool].connect( self.on_webview_loadFinished )
#        self.document.loadProgress[int].connect( self.on_webview_loadProgress )

    def reprint( self, printer ):
        self.padre.imprimir(printer)
    
    def accepted(self):
        self.padre.vistaprevia = False
        QPrintPreviewDialog.accepted(self)
        
    


