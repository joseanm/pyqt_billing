### -*- coding: utf-8 -*-
###!/usr/bin/env python
# This is only needed for Python v2 but is harmless for Python v3.
import sip
from xml.dom.minidom import Document
from Dialog import Dialog
sip.setapi('QVariant', 2)

from PyQt4 import QtCore, QtGui
from factura.factura import tbFactura
from factura.articulos import dlgArticulo
from herramientas.database import mydb
from ui.Ui_importaciones import Ui_MainWindow
import mdi_rc


class MdiChild(tbFactura):
    sequenceNumber = 1

    def __init__(self,parent):
        super(MdiChild, self).__init__()
        self.parent = parent
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.isUntitled = True
        

    def newFile(self):
        self.isUntitled = True
        self.curFile = "document%d.txt" % MdiChild.sequenceNumber
        MdiChild.sequenceNumber += 1
        self.setWindowTitle(self.curFile + '[*]')

#        self.document().contentsChanged.connect(self.documentWasModified)

    def loadFile(self, fileName):
        file = QtCore.QFile(fileName)
        if not file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
            QtGui.QMessageBox.warning(self, "MDI",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            return False

        instr = QtCore.QTextStream(file)
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.setPlainText(instr.readAll())
        QtGui.QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName)

        self.document().contentsChanged.connect(self.documentWasModified)

        return True

    def userFriendlyCurrentFile(self):
        return self.strippedName(self.curFile)

    def currentFile(self):
        return self.curFile

    def closeEvent(self, event):
        if self.maybeSave():
            event.accept()
        else:
            event.ignore()

    def documentWasModified(self):
        self.setWindowModified(self.document().isModified())

    def maybeSave(self):
#        if self.document().isModified():
#            ret = QtGui.QMessageBox.warning(self, "MDI",
#                    "'%s' has been modified.\nDo you want to save your "
#                    "changes?" % self.userFriendlyCurrentFile(),
#                    QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard |
#                    QtGui.QMessageBox.Cancel)
#            if ret == QtGui.QMessageBox.Save:
#                return self.save()
#            elif ret == QtGui.QMessageBox.Cancel:
#                return False

        return True

    def setCurrentFile(self, fileName):
        self.curFile = QtCore.QFileInfo(fileName).canonicalFilePath()
        self.isUntitled = False
        self.document().setModified(False)
        self.setWindowModified(False)
        self.setWindowTitle(self.userFriendlyCurrentFile() + "[*]")

    def strippedName(self, fullFileName):
        return QtCore.QFileInfo(fullFileName).fileName()


class MainWindow(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self.mdiArea)

        self.mdiArea.subWindowActivated.connect(self.updateMenus)
        self.windowMapper = QtCore.QSignalMapper(self)
        self.windowMapper.mapped[QtGui.QWidget].connect(self.setActiveSubWindow)
        
        self.newAct.triggered.connect(self.newFile)
        self.saveAct.triggered.connect(self.save)
        self.closeAct.triggered.connect(self.mdiArea.closeActiveSubWindow)
        self.closeAllAct.triggered.connect(self.mdiArea.closeAllSubWindows)
        self.tileAct.triggered.connect(self.mdiArea.tileSubWindows)
        self.cascadeAct.triggered.connect(self.mdiArea.cascadeSubWindows)
        self.nextAct.triggered.connect(self.mdiArea.activateNextSubWindow)
        self.previousAct.triggered.connect(self.mdiArea.activatePreviousSubWindow)
        self.actionEditar_Productos.triggered.connect(self.editarArticulos)
        self.exitAct.triggered.connect(self.close)
        self.aboutAct.triggered.connect(self.about)
        self.printAct.triggered.connect(self.printDocument)
        self.previewAct.triggered.connect(self.previewDoc)
#        self.fontAct.triggered.connect(self.fontEdit)

        self.updateMenus()

        self.readSettings()

        self.setWindowTitle("MDI")
        self.setUnifiedTitleAndToolBarOnMac(True)

    def closeEvent(self, event):
        self.mdiArea.closeAllSubWindows()
        if self.activeMdiChild():
            event.ignore()
        else:
            self.writeSettings()
            event.accept()

    def fontEdit(self):
        fontDialog = QtGui.QFontDialog()
        fontDialog.setCurrentFont( self.activeMdiChild().fuente)
        fontDialog.exec_()
        self.activeMdiChild().fuente = fontDialog.currentFont()

    def newFile(self):
        child = self.createMdiChild()
        child.newFile()
        child.showMaximized()

    def printDocument(self):
        self.activeMdiChild().printDocument()
        
    def previewDoc(self):
        if self.activeMdiChild() is not None:
            self.activeMdiChild().preview()
        
            

    def save(self):
        self.activeMdiChild().save()
 
    def about(self):
        QtGui.QMessageBox.about(self, "MIS Importaciones Pedro Mejia",
                u"<b>MIS Importaciones Pedro Mejia</b> es un sencillo sistema de facturación")

    def updateMenus(self):
        hasMdiChild = (self.activeMdiChild() is not None)
        self.saveAct.setEnabled(hasMdiChild)
        self.previewAct.setEnabled(hasMdiChild)
        self.printAct.setEnabled(hasMdiChild)
#        self.fontAct.setEnabled(False)
#        self.pasteAct.setEnabled(hasMdiChild)
        self.closeAct.setEnabled(hasMdiChild)
        self.closeAllAct.setEnabled(hasMdiChild)
        self.tileAct.setEnabled(hasMdiChild)
        self.cascadeAct.setEnabled(hasMdiChild)
        self.nextAct.setEnabled(hasMdiChild)
        self.previousAct.setEnabled(hasMdiChild)
#        self.separatorAct.setVisible(hasMdiChild)

#        self.cutAct.setEnabled(hasSelection)
#        self.copyAct.setEnabled(hasSelection)

    def updateWindowMenu(self):
        self.windowMenu.clear()
        self.windowMenu.addAction(self.closeAct)
        self.windowMenu.addAction(self.closeAllAct)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.tileAct)
        self.windowMenu.addAction(self.cascadeAct)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.nextAct)
        self.windowMenu.addAction(self.previousAct)
        self.windowMenu.addAction(self.separatorAct)

        windows = self.mdiArea.subWindowList()
        self.separatorAct.setVisible(len(windows) != 0)

        for i, window in enumerate(windows):
            child = window.widget()

            text = "%d %s" % (i + 1, child.userFriendlyCurrentFile())
            if i < 9:
                text = '&' + text

            action = self.windowMenu.addAction(text)
            action.setCheckable(True)
            action.setChecked(child == self.activeMdiChild())
            action.triggered.connect(self.windowMapper.map)
            self.windowMapper.setMapping(action, window)

    def createMdiChild(self):
        child = MdiChild(self)
        self.mdiArea.addSubWindow(child)
        return child
    
    def editarArticulos( self ):
        articulo = dlgArticulo(self)
        articulo.exec_()

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addSeparator()
        action = self.fileMenu.addAction("Switch layout direction")
        action.triggered.connect(self.switchLayoutDirection)
        self.fileMenu.addAction(self.exitAct)

#        self.editMenu = self.menuBar().addMenu("&Edit")
#        self.editMenu.addAction(self.cutAct)
#        self.editMenu.addAction(self.copyAct)
#        self.editMenu.addAction(self.pasteAct)


        self.productMenu = self.menuBar().addMenu("&Productos")
        self.productMenu.addAction(self.articuloAct)

        self.windowMenu = self.menuBar().addMenu("&Window")
        self.updateWindowMenu()
        self.windowMenu.aboutToShow.connect(self.updateWindowMenu)

        self.menuBar().addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def createToolBars(self):
        self.fileToolBar = self.addToolBar("File")
        self.fileToolBar.addAction(self.newAct)
        self.fileToolBar.addAction(self.openAct)
        self.fileToolBar.addAction(self.saveAct)

#        self.editToolBar = self.addToolBar("Edit")
#        self.editToolBar.addAction(self.cutAct)
#        self.editToolBar.addAction(self.copyAct)
#        self.editToolBar.addAction(self.pasteAct)

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def readSettings(self):
        settings = QtCore.QSettings('Trolltech', 'MDI Example')
        pos = settings.value('pos', QtCore.QPoint(200, 200))
        size = settings.value('size', QtCore.QSize(400, 400))
        self.move(pos)
        self.resize(size)

    def writeSettings(self):
        settings = QtCore.QSettings('Trolltech', 'MDI Example')
        settings.setValue('pos', self.pos())
        settings.setValue('size', self.size())

    def activeMdiChild(self):
        activeSubWindow = self.mdiArea.activeSubWindow()
        if activeSubWindow:
            return activeSubWindow.widget()
        return None

    def findMdiChild(self, fileName):
        canonicalFilePath = QtCore.QFileInfo(fileName).canonicalFilePath()

        for window in self.mdiArea.subWindowList():
            if window.widget().currentFile() == canonicalFilePath:
                return window
        return None

    def switchLayoutDirection(self):
        if self.layoutDirection() == QtCore.Qt.LeftToRight:
            QtGui.qApp.setLayoutDirection(QtCore.Qt.RightToLeft)
        else:
            QtGui.qApp.setLayoutDirection(QtCore.Qt.LeftToRight)

    def setActiveSubWindow(self, window):
        if window:
            self.mdiArea.setActiveSubWindow(window)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.database = mydb().database
    mainWin.showMaximized()

    
    sys.exit(app.exec_())
