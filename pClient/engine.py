import os
from funArea import areaStrToList # pylint: disable=no-name-in-module, import-error
import pyscreenshot as ImageGrab 
import cv2
import numpy as np
import pytesseract 
import pyautogui
import time

class Engine():
    def __init__(self, commandList):
        self.commandList = commandList

    def getAutoObjectByName(self, name):
        for el in self.commandList:
            if el.name == name:
                return True, el
        return False, 0


    # pylint: disable=no-member
    def find_patt(self, image, patt, thres):
        img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_grey, patt, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res > thres)
        return zip(*loc[::-1])
    # pylint: enable=no-member


    def isArea(self, autoObject):
        fileName = "img\\"+autoObject.name+".jpg"
        if not os.path.exists(fileName):
            print("no file: " + fileName)
            return False
        # area1 = areaStrToList(autoObject.area1)
        area2 = areaStrToList(autoObject.area2)

        # img_find_in = np.array(ImageGrab.grab(bbox=(area2[0],area2[1],area2[2],area2[3])))
        screenshot = ImageGrab.grab(bbox=(area2[0],area2[1],area2[2],area2[3]))
        img_find_in = np.array(screenshot.getdata(), dtype='uint8').reshape(
            (screenshot.size[1], screenshot.size[0], 3))
        
        img_find_what = cv2.imread(fileName,0) # pylint: disable=no-member

        points = self.find_patt(img_find_in, img_find_what, 0.60)
        pointsl = list(points)

        return len(pointsl) != 0

    def isAreaByName(self, name):
        isObj, autoObject  = self.getAutoObjectByName(name)
        if isObj:
            return self.isArea(autoObject)
        else:
            return False

    def getAreaCoord(self, autoObject):
        fileName = "img\\"+autoObject.name+".jpg"
        if not os.path.exists(fileName):
            print("no file: " + fileName)
            return False
        # area1 = areaStrToList(autoObject.area1)
        area2 = areaStrToList(autoObject.area2)

        # img_find_in = np.array(ImageGrab.grab(bbox=(area2[0],area2[1],area2[2],area2[3])))
        screenshot = ImageGrab.grab(bbox=(area2[0],area2[1],area2[2],area2[3]))
        img_find_in = np.array(screenshot.getdata(), dtype='uint8').reshape(
            (screenshot.size[1], screenshot.size[0], 3))
        
        img_find_what = cv2.imread(fileName,0) # pylint: disable=no-member

        points = self.find_patt(img_find_in, img_find_what, 0.60)
        pointsl = list(points)

        if len(pointsl) == 0:
            return False, [0,0]
        else:
            return True, pointsl[0]

    def getAreaCoordByName(self, name):
        isObj, autoObject  = self.getAutoObjectByName(name)
        if isObj:
            return self.getAreaCoord(autoObject)
        else:
            return False , [0,0]

    def getText(self, autoObject):
        area1 = areaStrToList(autoObject.area1)
    
        screenshot = np.array(ImageGrab.grab(bbox=(area1[0],area1[1],area1[2],area1[3])))
        
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY) # pylint: disable=no-member
        screenshot = cv2.bitwise_not(screenshot) # pylint: disable=no-member
        screenshot = cv2.threshold(screenshot, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] # pylint: disable=no-member
        # _, screenshot = cv2.threshold(screenshot, 180, 255, cv2.THRESH_BINARY)
        screenshot = cv2.medianBlur(screenshot, 3) # pylint: disable=no-member
        # screenshot = cv2.resize(screenshot,(35,20))
        # cv2.namedWindow('image')   # pylint: disable=no-member
        # cv2.imshow("image", screenshot) # pylint: disable=no-member
        # return False
        return pytesseract.image_to_string(screenshot, config='--psm 6 -c tessedit_char_whitelist=0123456789')

    def strToInt(self, str):
        # print("<--"+str)
        result = ""
        for s in str:
            if s in ('0','1','2','3','4','5','6','7','8','9'):
                result = result + s
        # print("-->"+result)
        if len(result) == 0:
            return 0
        return int(result)

    def getTextByName(self, name):
        isObj, autoObject  = self.getAutoObjectByName(name)
        if isObj:
            return self.getText(autoObject)
        else:
            return ""

    def clickToArea(self, autoObject):
        area1 = areaStrToList(autoObject.area1)
        x = int((area1[0] + area1[2])/2)
        y = int((area1[1] + area1[3])/2)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.5)

    def clickToAreaByName(self, name):
        isObj, autoObject  = self.getAutoObjectByName(name)
        if isObj:
            self.clickToArea(autoObject)