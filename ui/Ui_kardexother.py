# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kardexother.ui'
#
# Created by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FrmKardexOther(object):
    def setupUi(self, FrmKardexOther):
        FrmKardexOther.setObjectName(_fromUtf8("FrmKardexOther"))
        FrmKardexOther.resize(644, 600)
        self.centralwidget = QtGui.QWidget(FrmKardexOther)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabdetails = QtGui.QWidget()
        self.tabdetails.setObjectName(_fromUtf8("tabdetails"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tabdetails)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_2 = QtGui.QLabel(self.tabdetails)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_6.addWidget(self.label_2)
        self.txtPrintedDocumentNumber = QtGui.QLineEdit(self.tabdetails)
        self.txtPrintedDocumentNumber.setReadOnly(True)
        self.txtPrintedDocumentNumber.setObjectName(_fromUtf8("txtPrintedDocumentNumber"))
        self.horizontalLayout_6.addWidget(self.txtPrintedDocumentNumber)
        self.label_5 = QtGui.QLabel(self.tabdetails)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        self.dtPicker = QtGui.QDateTimeEdit(self.tabdetails)
        self.dtPicker.setReadOnly(True)
        self.dtPicker.setCalendarPopup(True)
        self.dtPicker.setObjectName(_fromUtf8("dtPicker"))
        self.horizontalLayout_6.addWidget(self.dtPicker)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.tabdetails)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.swConcept = QtGui.QStackedWidget(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swConcept.sizePolicy().hasHeightForWidth())
        self.swConcept.setSizePolicy(sizePolicy)
        self.swConcept.setObjectName(_fromUtf8("swConcept"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.page_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.txtConcept = QtGui.QLineEdit(self.page_3)
        self.txtConcept.setReadOnly(True)
        self.txtConcept.setObjectName(_fromUtf8("txtConcept"))
        self.horizontalLayout_3.addWidget(self.txtConcept)
        self.swConcept.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.cbConcept = QtGui.QComboBox(self.page_4)
        self.cbConcept.setEditable(True)
        self.cbConcept.setObjectName(_fromUtf8("cbConcept"))
        self.verticalLayout_3.addWidget(self.cbConcept)
        self.swConcept.addWidget(self.page_4)
        self.horizontalLayout_2.addWidget(self.swConcept)
        self.label_4 = QtGui.QLabel(self.tabdetails)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.swWarehouse = QtGui.QStackedWidget(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swWarehouse.sizePolicy().hasHeightForWidth())
        self.swWarehouse.setSizePolicy(sizePolicy)
        self.swWarehouse.setObjectName(_fromUtf8("swWarehouse"))
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.page_5)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.txtWarehouse = QtGui.QLineEdit(self.page_5)
        self.txtWarehouse.setReadOnly(True)
        self.txtWarehouse.setObjectName(_fromUtf8("txtWarehouse"))
        self.verticalLayout_5.addWidget(self.txtWarehouse)
        self.swWarehouse.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page_6)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.cbWarehouse = QtGui.QComboBox(self.page_6)
        self.cbWarehouse.setEditable(True)
        self.cbWarehouse.setObjectName(_fromUtf8("cbWarehouse"))
        self.verticalLayout_4.addWidget(self.cbWarehouse)
        self.swWarehouse.addWidget(self.page_6)
        self.horizontalLayout_2.addWidget(self.swWarehouse)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.splitter_2 = QtGui.QSplitter(self.tabdetails)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setOpaqueResize(True)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.tabledetails = QtGui.QTableView(self.splitter_2)
        self.tabledetails.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tabledetails.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabledetails.setAlternatingRowColors(True)
        self.tabledetails.setObjectName(_fromUtf8("tabledetails"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_7.addWidget(self.label_6)
        self.txtObservations = QtGui.QPlainTextEdit(self.layoutWidget)
        self.txtObservations.setObjectName(_fromUtf8("txtObservations"))
        self.verticalLayout_7.addWidget(self.txtObservations)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.lblaccounts = QtGui.QLabel(self.layoutWidget1)
        self.lblaccounts.setObjectName(_fromUtf8("lblaccounts"))
        self.verticalLayout_6.addWidget(self.lblaccounts)
        self.tableaccounts = QtGui.QTableView(self.layoutWidget1)
        self.tableaccounts.setObjectName(_fromUtf8("tableaccounts"))
        self.verticalLayout_6.addWidget(self.tableaccounts)
        self.verticalLayout_8.addWidget(self.splitter_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/document-edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabdetails, icon, _fromUtf8(""))
        self.tabnavigation = QtGui.QWidget()
        self.tabnavigation.setObjectName(_fromUtf8("tabnavigation"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabnavigation)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tablenavigation = QtGui.QTableView(self.tabnavigation)
        self.tablenavigation.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tablenavigation.setAlternatingRowColors(True)
        self.tablenavigation.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablenavigation.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablenavigation.setSortingEnabled(True)
        self.tablenavigation.setObjectName(_fromUtf8("tablenavigation"))
        self.tablenavigation.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tablenavigation)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tabnavigation)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.tabnavigation)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/table.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabnavigation, icon1, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        FrmKardexOther.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(FrmKardexOther)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        FrmKardexOther.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.label_2.setBuddy(self.txtPrintedDocumentNumber)
        self.label_5.setBuddy(self.dtPicker)
        self.label_3.setBuddy(self.cbConcept)
        self.label_4.setBuddy(self.cbWarehouse)
        self.label_6.setBuddy(self.txtObservations)
        self.lblaccounts.setBuddy(self.tableaccounts)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(FrmKardexOther)
        self.tabWidget.setCurrentIndex(1)
        self.swConcept.setCurrentIndex(0)
        self.swWarehouse.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FrmKardexOther)
        FrmKardexOther.setTabOrder(self.txtPrintedDocumentNumber, self.dtPicker)
        FrmKardexOther.setTabOrder(self.dtPicker, self.cbConcept)
        FrmKardexOther.setTabOrder(self.cbConcept, self.cbWarehouse)
        FrmKardexOther.setTabOrder(self.cbWarehouse, self.tabledetails)
        FrmKardexOther.setTabOrder(self.tabledetails, self.txtObservations)
        FrmKardexOther.setTabOrder(self.txtObservations, self.tableaccounts)
        FrmKardexOther.setTabOrder(self.tableaccounts, self.tabWidget)
        FrmKardexOther.setTabOrder(self.tabWidget, self.txtWarehouse)
        FrmKardexOther.setTabOrder(self.txtWarehouse, self.txtConcept)
        FrmKardexOther.setTabOrder(self.txtConcept, self.tablenavigation)
        FrmKardexOther.setTabOrder(self.tablenavigation, self.lineEdit)

    def retranslateUi(self, FrmKardexOther):
        FrmKardexOther.setWindowTitle(QtGui.QApplication.translate("FrmKardexOther", "Otros Movimientos de Kardex", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FrmKardexOther", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&amp;Numero de Ajuste de Bodega:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FrmKardexOther", "<b>&Fecha</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FrmKardexOther", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">&amp;Concepto:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FrmKardexOther", "<b>&Bodega</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("FrmKardexOther", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Comentario&amp;s</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblaccounts.setText(QtGui.QApplication.translate("FrmKardexOther", "<b>&Movimientos</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FrmKardexOther", "&Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("FrmKardexOther", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FrmKardexOther = QtGui.QMainWindow()
    ui = Ui_FrmKardexOther()
    ui.setupUi(FrmKardexOther)
    FrmKardexOther.show()
    sys.exit(app.exec_())

