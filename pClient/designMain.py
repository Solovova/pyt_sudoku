# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tabObjects = QtWidgets.QWidget()
        self.tabObjects.setObjectName("tabObjects")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabObjects)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tabObjects)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnObjectsAdd = QtWidgets.QPushButton(self.tabObjects)
        self.btnObjectsAdd.setObjectName("btnObjectsAdd")
        self.horizontalLayout.addWidget(self.btnObjectsAdd)
        self.btnObjectsEdit = QtWidgets.QPushButton(self.tabObjects)
        self.btnObjectsEdit.setObjectName("btnObjectsEdit")
        self.horizontalLayout.addWidget(self.btnObjectsEdit)
        self.pushButton_Test = QtWidgets.QPushButton(self.tabObjects)
        self.pushButton_Test.setObjectName("pushButton_Test")
        self.horizontalLayout.addWidget(self.pushButton_Test)
        self.btn_sud_simple = QtWidgets.QPushButton(self.tabObjects)
        self.btn_sud_simple.setObjectName("btn_sud_simple")
        self.horizontalLayout.addWidget(self.btn_sud_simple)
        self.btn_sud_battle = QtWidgets.QPushButton(self.tabObjects)
        self.btn_sud_battle.setObjectName("btn_sud_battle")
        self.horizontalLayout.addWidget(self.btn_sud_battle)
        self.btn_sud_simple_scrshot = QtWidgets.QPushButton(self.tabObjects)
        self.btn_sud_simple_scrshot.setObjectName("btn_sud_simple_scrshot")
        self.horizontalLayout.addWidget(self.btn_sud_simple_scrshot)
        self.btn_sud_battle_scrshot = QtWidgets.QPushButton(self.tabObjects)
        self.btn_sud_battle_scrshot.setObjectName("btn_sud_battle_scrshot")
        self.horizontalLayout.addWidget(self.btn_sud_battle_scrshot)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnObjectsDelete = QtWidgets.QPushButton(self.tabObjects)
        self.btnObjectsDelete.setObjectName("btnObjectsDelete")
        self.horizontalLayout.addWidget(self.btnObjectsDelete)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.push_button_sud_new = QtWidgets.QPushButton(self.tabObjects)
        self.push_button_sud_new.setObjectName("push_button_sud_new")
        self.verticalLayout_2.addWidget(self.push_button_sud_new)
        self.tabWidget.addTab(self.tabObjects, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButtonOcrLoadShow = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonOcrLoadShow.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButtonOcrLoadShow.setObjectName("pushButtonOcrLoadShow")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Area1"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Area2"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Test"))
        self.btnObjectsAdd.setText(_translate("MainWindow", "Add"))
        self.btnObjectsEdit.setText(_translate("MainWindow", "Edit"))
        self.pushButton_Test.setText(_translate("MainWindow", "Test"))
        self.btn_sud_simple.setText(_translate("MainWindow", "Simple"))
        self.btn_sud_battle.setText(_translate("MainWindow", "Battle"))
        self.btn_sud_simple_scrshot.setText(_translate("MainWindow", "Simple_Scrshot"))
        self.btn_sud_battle_scrshot.setText(_translate("MainWindow", "Battle_Scrshot"))
        self.btnObjectsDelete.setText(_translate("MainWindow", "Del"))
        self.push_button_sud_new.setText(_translate("MainWindow", "Sudoku new"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabObjects), _translate("MainWindow", "Objects"))
        self.pushButtonOcrLoadShow.setText(_translate("MainWindow", "Load@Show"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Страница"))
