from PyQt5 import QtWidgets

import designMain
import os
import configparser
import time
from TreadWorker import TreadWorker
from pClient.autoObject.autoObject import AutoObject
from pClient.dialogObject.dialogObject import DialogObject
from pClient.engine import Engine


class GuiApp(QtWidgets.QMainWindow, designMain.Ui_MainWindow):
    listAutoObject = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.loadList()
        self.fillTable()

        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.btnObjectsAdd.clicked.connect(self.clc_btnObjectsAdd)
        self.btnObjectsEdit.clicked.connect(self.clc_btnObjectsEdit)
        self.btnObjectsDelete.clicked.connect(self.clc_btnObjectsDelete)
        self.btnObjectsTest.clicked.connect(self.clc_btn_objects_test)
        self.tableWidget.doubleClicked.connect(self.clc_btnObjectsEdit)
        self.initThread()

    def loadList(self):
        if not os.path.exists("settings.ini"):
            return
        config = configparser.ConfigParser()
        config.read("settings.ini")
        ind = 0
        while True:
            if not config.has_option("Objects", str(ind) + "_type1"):
                break
            type1 = config.get("Objects", str(ind) + "_type1")
            name = config.get("Objects", str(ind) + "_name")
            area1 = config.get("Objects", str(ind) + "_area1")
            area2 = config.get("Objects", str(ind) + "_area2")
            autoObject = AutoObject(type1, name, area1, area2)
            self.listAutoObject.append(autoObject)
            ind = ind + 1

    def saveList(self):
        config = configparser.ConfigParser()
        config.add_section("Objects")
        ind = 0
        for el in self.listAutoObject:
            config.set("Objects", str(ind) + "_type1", el.type1)
            config.set("Objects", str(ind) + "_name", el.name)
            config.set("Objects", str(ind) + "_area1", el.area1)
            config.set("Objects", str(ind) + "_area2", el.area2)
            ind = ind + 1

        with open("settings.ini", "w") as config_file:
            config.write(config_file)

    def fillTable(self):
        self.tableWidget.setRowCount(0)
        for el in self.listAutoObject:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(
                rowPosition, 0, QtWidgets.QTableWidgetItem(el.type1))
            self.tableWidget.setItem(
                rowPosition, 1, QtWidgets.QTableWidgetItem(el.name))
            self.tableWidget.setItem(
                rowPosition, 2, QtWidgets.QTableWidgetItem(el.area1))
            self.tableWidget.setItem(
                rowPosition, 3, QtWidgets.QTableWidgetItem(el.area2))
        self.tableWidget.resizeColumnsToContents()

    def clc_btnObjectsAdd(self):
        print("add")
        dlg = DialogObject()
        dlg.exec_()

        if (dlg.isOk):
            autoObject = AutoObject(str(dlg.cbType.currentText()), dlg.txtName.text(
            ), dlg.txtArea1.text(), dlg.txtArea2.text())
            self.listAutoObject.append(autoObject)
            self.fillTable()

    def clc_btnObjectsEdit(self):
        if (self.tableWidget.currentRow() != -1):
            dlg = DialogObject()
            dlg.setData(self.listAutoObject[self.tableWidget.currentRow()])
            dlg.exec_()
            if (dlg.isOk):
                autoObject = AutoObject(str(dlg.cbType.currentText()), dlg.txtName.text(
                ), dlg.txtArea1.text(), dlg.txtArea2.text())
                self.listAutoObject[self.tableWidget.currentRow()] = autoObject
                self.fillTable()

        print("edit:" + str(self.tableWidget.currentRow()))

    def clc_btnObjectsDelete(self):
        curRow = self.tableWidget.currentRow()
        if (curRow != -1):
            self.listAutoObject.remove(
                self.listAutoObject[self.tableWidget.currentRow()])
            self.fillTable()
            if (curRow >= self.tableWidget.rowCount()):
                if (self.tableWidget.rowCount() != 0):
                    self.tableWidget.selectRow(self.tableWidget.rowCount() - 1)
            else:
                self.tableWidget.selectRow(curRow)

    def clc_btn_objects_test(self):
        Engine(self.listAutoObject).test_sudoku()


        # if (self.tableWidget.currentRow() != -1):
        # testResult = Engine(self.listAutoObject).getAreaCoord(self.listAutoObject[self.tableWidget.currentRow()])

        # testResult = Engine(self.listAutoObject).isArea(self.listAutoObject[self.tableWidget.currentRow()])
        # testResult = str(int(Engine(self.listAutoObject).getText(self.listAutoObject[self.tableWidget.currentRow()])))
        # print(testResult)
        # self.tableWidget.setItem(self.tableWidget.currentRow(), 4, QtWidgets.QTableWidgetItem(testResult))
        # self.tableWidget.resizeColumnsToContents()

    def initThread(self):
        self.treadWorker = TreadWorker(self)
        self.treadWorker.signal.connect(self.SignalTreadWorker)
        self.treadWorker.start()

    def SignalTreadWorker(self, data):
        print("Signal")
