# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/creditodebito.ui'
#
# Created: Mon Aug 23 03:35:52 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_frmCreditoDebito(object):
    def setupUi(self, FrmCreditoDebito):
        FrmCreditoDebito.setObjectName("frmCreditoDebito")
        FrmCreditoDebito.resize(800, 600)
        FrmCreditoDebito.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtGui.QWidget(FrmCreditoDebito)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tabdetails = QtGui.QWidget()
        self.tabdetails.setObjectName("tabdetails")
        self.gridLayout = QtGui.QGridLayout(self.tabdetails)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txtDocumentNumber = QtGui.QLineEdit(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDocumentNumber.sizePolicy().hasHeightForWidth())
        self.txtDocumentNumber.setSizePolicy(sizePolicy)
        self.txtDocumentNumber.setReadOnly(True)
        self.txtDocumentNumber.setObjectName("txtDocumentNumber")
        self.horizontalLayout_2.addWidget(self.txtDocumentNumber)
        self.label_3 = QtGui.QLabel(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.stackedWidget = QtGui.QStackedWidget(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cbClient = QtGui.QComboBox(self.page_5)
        self.cbClient.setObjectName("cbClient")
        self.verticalLayout_3.addWidget(self.cbClient)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName("page_6")
        self.txtClient = QtGui.QLineEdit(self.page_6)
        self.txtClient.setGeometry(QtCore.QRect(4, 4, 105, 25))
        self.txtClient.setReadOnly(True)
        self.txtClient.setObjectName("txtClient")
        self.stackedWidget.addWidget(self.page_6)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.label_4 = QtGui.QLabel(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.txtBill = QtGui.QLineEdit(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtBill.sizePolicy().hasHeightForWidth())
        self.txtBill.setSizePolicy(sizePolicy)
        self.txtBill.setReadOnly(True)
        self.txtBill.setObjectName("txtBill")
        self.horizontalLayout_2.addWidget(self.txtBill)
        self.label_5 = QtGui.QLabel(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.dtPicker = QtGui.QDateTimeEdit(self.tabdetails)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dtPicker.sizePolicy().hasHeightForWidth())
        self.dtPicker.setSizePolicy(sizePolicy)
        self.dtPicker.setReadOnly(True)
        self.dtPicker.setCalendarPopup(True)
        self.dtPicker.setObjectName("dtPicker")
        self.horizontalLayout_2.addWidget(self.dtPicker)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.tabledetails = QtGui.QTableView(self.tabdetails)
        self.tabledetails.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabledetails.setObjectName("tabledetails")
        self.tabledetails.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tabledetails, 1, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(self.tabdetails)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.txtObservations = QtGui.QPlainTextEdit(self.groupBox_2)
        self.txtObservations.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtObservations.sizePolicy().hasHeightForWidth())
        self.txtObservations.setSizePolicy(sizePolicy)
        self.txtObservations.setReadOnly(True)
        self.txtObservations.setObjectName("txtObservations")
        self.gridLayout_3.addWidget(self.txtObservations, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.tabdetails)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.lblTaxes = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTaxes.sizePolicy().hasHeightForWidth())
        self.lblTaxes.setSizePolicy(sizePolicy)
        self.lblTaxes.setObjectName("lblTaxes")
        self.gridLayout_2.addWidget(self.lblTaxes, 1, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)
        self.lblCost = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCost.sizePolicy().hasHeightForWidth())
        self.lblCost.setSizePolicy(sizePolicy)
        self.lblCost.setObjectName("lblCost")
        self.gridLayout_2.addWidget(self.lblCost, 2, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)
        self.lblTotal = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTotal.sizePolicy().hasHeightForWidth())
        self.lblTotal.setSizePolicy(sizePolicy)
        self.lblTotal.setObjectName("lblTotal")
        self.gridLayout_2.addWidget(self.lblTotal, 3, 1, 1, 1)
        self.lblSubtotal = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSubtotal.sizePolicy().hasHeightForWidth())
        self.lblSubtotal.setSizePolicy(sizePolicy)
        self.lblSubtotal.setObjectName("lblSubtotal")
        self.gridLayout_2.addWidget(self.lblSubtotal, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 1, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabdetails, icon, "")
        self.tabnavigation = QtGui.QWidget()
        self.tabnavigation.setObjectName("tabnavigation")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabnavigation)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tablenavigation = QtGui.QTableView(self.tabnavigation)
        self.tablenavigation.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tablenavigation.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablenavigation.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablenavigation.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablenavigation.setSortingEnabled(True)
        self.tablenavigation.setObjectName("tablenavigation")
        self.tablenavigation.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tablenavigation)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.tabnavigation)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtSearch = QtGui.QLineEdit(self.tabnavigation)
        self.txtSearch.setObjectName("txtSearch")
        self.horizontalLayout.addWidget(self.txtSearch)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabnavigation, icon1, "")
        self.verticalLayout.addWidget(self.tabWidget)
        FrmCreditoDebito.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(FrmCreditoDebito)
        self.statusbar.setObjectName("statusbar")
        FrmCreditoDebito.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(FrmCreditoDebito)
        self.toolBar.setObjectName("toolBar")
        FrmCreditoDebito.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.label_2.setBuddy(self.txtDocumentNumber)
        self.label_3.setBuddy(self.txtBill)
        self.label_4.setBuddy(self.txtClient)
        self.label_5.setBuddy(self.dtPicker)
        self.label.setBuddy(self.txtSearch)

        self.retranslateUi(FrmCreditoDebito)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FrmCreditoDebito)
        FrmCreditoDebito.setTabOrder(self.txtDocumentNumber, self.dtPicker)
        FrmCreditoDebito.setTabOrder(self.dtPicker, self.tabledetails)
        FrmCreditoDebito.setTabOrder(self.tabledetails, self.txtObservations)
        FrmCreditoDebito.setTabOrder(self.txtObservations, self.txtBill)
        FrmCreditoDebito.setTabOrder(self.txtBill, self.txtClient)
        FrmCreditoDebito.setTabOrder(self.txtClient, self.cbClient)
        FrmCreditoDebito.setTabOrder(self.cbClient, self.tabWidget)
        FrmCreditoDebito.setTabOrder(self.tabWidget, self.tablenavigation)
        FrmCreditoDebito.setTabOrder(self.tablenavigation, self.txtSearch)

    def retranslateUi(self, FrmCreditoDebito):
        FrmCreditoDebito.setWindowTitle(QtGui.QApplication.translate("frmCreditoDebito", "Notas Debito/Credito", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("frmCreditoDebito", "# Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("frmCreditoDebito", "Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("frmCreditoDebito", "# Devolucion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("frmCreditoDebito", "Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("frmCreditoDebito", "Observaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("frmCreditoDebito", "Totales", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("frmCreditoDebito", "Subtotal: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("frmCreditoDebito", "Impuesto: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTaxes.setText(QtGui.QApplication.translate("frmCreditoDebito", "C$ 0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("frmCreditoDebito", "Costo Total: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCost.setText(QtGui.QApplication.translate("frmCreditoDebito", "C$ 0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("frmCreditoDebito", "Total Devolución: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTotal.setText(QtGui.QApplication.translate("frmCreditoDebito", "C$ 0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSubtotal.setText(QtGui.QApplication.translate("frmCreditoDebito", "C$ 0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabdetails), None)
        self.label.setText(QtGui.QApplication.translate("frmCreditoDebito", "&Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabnavigation), None)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("frmCreditoDebito", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FrmCreditoDebito = QtGui.QMainWindow()
    ui = Ui_frmCreditoDebito()
    ui.setupUi(FrmCreditoDebito)
    FrmCreditoDebito.show()
    sys.exit(app.exec_())

