from PIL import ImageGrab
from PyQt5 import QtWidgets
import cv2
import numpy as np

from ext_funks.area_str_to_list import area_str_to_list
from pClient.dialogObject.designDialogObject import Ui_Dialog
from pClient.funCV.cvGetArea import GetArea


class DialogObject(QtWidgets.QDialog, Ui_Dialog):
    isOk = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnOk.clicked.connect(self.clc_btnOk)
        self.btnCancel.clicked.connect(self.clc_btnCancel)
        self.btnArea1.clicked.connect(self.clc_btnArea1)
        self.btnArea2.clicked.connect(self.clc_btnArea2)
        self.btnGrab.clicked.connect(self.clc_btnGrabArea1)

    def setData(self, el):
        index = self.cbType.findText(el.type1)
        if index != -1:
            self.cbType.setCurrentIndex(index)

        self.txtName.setText(el.name)
        self.txtArea1.setText(el.area1)
        self.txtArea2.setText(el.area2)

    def clc_btnOk(self):
        self.isOk = True
        self.close()

    def clc_btnCancel(self):
        self.close()

    def clc_btnArea1(self):
        self.txtArea1.setText(str(GetArea().getArea(area_str_to_list(self.txtArea1.text()))))

    def clc_btnArea2(self):
        self.txtArea2.setText(str(GetArea().getArea(area_str_to_list(self.txtArea2.text()))))

    def clc_btnGrabArea1(self):
        lst = area_str_to_list(self.txtArea1.text())
        img_grab = ImageGrab.grab(bbox=(lst[0], lst[1], lst[2], lst[3]))
        img_save = cv2.cvtColor(np.array(img_grab), cv2.COLOR_RGB2BGR)  # pylint: disable=no-member
        name = "img\\" + self.txtName.text() + ".jpg"
        print(name)
        cv2.imwrite(name, img_save)  # pylint: disable=no-member
        print("grab")
