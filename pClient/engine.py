import os
from funArea import areaStrToList  # pylint: disable=no-name-in-module, import-error
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
        fileName = "img\\" + autoObject.name + ".jpg"
        if not os.path.exists(fileName):
            print("no file: " + fileName)
            return False
        # area1 = areaStrToList(autoObject.area1)
        area2 = areaStrToList(autoObject.area2)

        # img_find_in = np.array(ImageGrab.grab(bbox=(area2[0],area2[1],area2[2],area2[3])))
        screenshot = ImageGrab.grab(bbox=(area2[0], area2[1], area2[2], area2[3]))
        img_find_in = np.array(screenshot.getdata(), dtype='uint8').reshape(
            (screenshot.size[1], screenshot.size[0], 3))

        img_find_what = cv2.imread(fileName, 0)  # pylint: disable=no-member

        points = self.find_patt(img_find_in, img_find_what, 0.60)
        pointsl = list(points)

        return len(pointsl) != 0

    def isAreaByName(self, name):
        isObj, autoObject = self.getAutoObjectByName(name)
        if isObj:
            return self.isArea(autoObject)
        else:
            return False

    def getAreaCoord(self, autoObject):
        fileName = "img\\" + autoObject.name + ".jpg"
        if not os.path.exists(fileName):
            print("no file: " + fileName)
            return False
        # area1 = areaStrToList(autoObject.area1)
        area2 = areaStrToList(autoObject.area2)

        # img_find_in = np.array(ImageGrab.grab(bbox=(area2[0],area2[1],area2[2],area2[3])))
        screenshot = ImageGrab.grab(bbox=(area2[0], area2[1], area2[2], area2[3]))
        img_find_in = np.array(screenshot.getdata(), dtype='uint8').reshape(
            (screenshot.size[1], screenshot.size[0], 3))

        img_find_what = cv2.imread(fileName, 0)  # pylint: disable=no-member

        points = self.find_patt(img_find_in, img_find_what, 0.60)
        pointsl = list(points)

        if len(pointsl) == 0:
            return False, [0, 0]
        else:
            return True, pointsl[0]

    def getAreaCoordByName(self, name):
        isObj, autoObject = self.getAutoObjectByName(name)
        if isObj:
            return self.getAreaCoord(autoObject)
        else:
            return False, [0, 0]

    def get_subarea(self, area: list[int], x: int, y: int, dimension: int) -> list[int]:
        wx: int = (area[2] - area[0]) // dimension
        wy: int = (area[3] - area[1]) // dimension
        sx: int = area[0] + wx * x
        sy: int = area[1] + wy * y

        return list([sx, sy, sx + wx, sy + wy])

    def get_sudoku(self) -> bool:
        sudoku_object_name: str = "sudTest"
        is_find, auto_object = self.getAutoObjectByName(sudoku_object_name)
        if not is_find:
            print(f'Not find object {sudoku_object_name}')
            return False
        area1 = areaStrToList(auto_object.area1)
        dimension: int = 9

        # x: int = 5
        # y: int = 2
        # subarea = self.get_subarea(area1, x, y, dimension)
        # # print(f'({x},{y}) {subarea}')
        # print(f'({x},{y}) "{self.get_sudoku_digit(subarea, "name")}"')

        sudoku_list: list[str] = ["" for _ in range(9)]

        for x in range(dimension):
            for y in range(dimension):
                subarea = self.get_subarea(area1, x, y, dimension)
                # print(f'({x},{y}) {subarea}')
                # print(f'({x},{y}) {self.get_sudoku_digit(subarea)}')
                tmp = self.get_sudoku_digit(subarea)
                if tmp == 0:
                    tmp_str = " "
                else:
                    tmp_str = str(tmp)
                sudoku_list[y] = sudoku_list[y] + tmp_str

        print(sudoku_list)
        # print(area1)

    def sudoku_str_to_int(self, str):
        # print("<--"+str)
        result = ""
        for s in str:
            if s in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                result = result + s
        # print("-->"+result)
        if len(result) == 0:
            return 0
        return int(result)

    def sudoku_get_without_border(self, arr, border: int):
        wy = len(arr)
        wx = len(arr[0])
        return arr[border:wx - border, border:wy - border]

    def sudoku_is_number(self, arr) -> bool:
        return np.average(arr, axis=None, weights=None, returned=False) > 5

    def get_sudoku_digit(self, area, name_window: str = ""):
        screenshot = np.array(ImageGrab.grab(bbox=(area[0], area[1], area[2], area[3])))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)  # pylint: disable=no-member
        # screenshot = cv2.bitwise_not(screenshot)  # pylint: disable=no-member
        # screenshot = cv2.threshold(screenshot, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        screenshot = cv2.medianBlur(screenshot, 3)  # pylint: disable=no-member
        # screenshot = self.sudoku_get_without_border(screenshot, 2)

        if name_window != "":
            cv2.namedWindow(name_window)  # pylint: disable=no-member
            cv2.imshow(name_window, screenshot)  # pylint: disable=no-member

        custom_config = r'--oem 3 --psm 10 outputbase digits'
        # , timeout=0.5
        # , config=custom_config
        rec_str = pytesseract.image_to_string(screenshot, config="--oem 3  --psm 6 outputbase digits")
        print(f'rec:"{rec_str}"')
        return self.sudoku_str_to_int(rec_str)

    def getText(self, autoObject):
        area1 = areaStrToList(autoObject.area1)
        print(area1)

        screenshot = np.array(ImageGrab.grab(bbox=(area1[0], area1[1], area1[2], area1[3])))

        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)  # pylint: disable=no-member
        screenshot = cv2.bitwise_not(screenshot)  # pylint: disable=no-member
        screenshot = cv2.threshold(screenshot, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[
            1]  # pylint: disable=no-member
        # _, screenshot = cv2.threshold(screenshot, 180, 255, cv2.THRESH_BINARY)
        screenshot = cv2.medianBlur(screenshot, 3)  # pylint: disable=no-member
        # screenshot = cv2.resize(screenshot,(35,20))
        # cv2.namedWindow('image')   # pylint: disable=no-member
        # cv2.imshow("image", screenshot) # pylint: disable=no-member
        # return False
        return pytesseract.image_to_string(screenshot, config='--psm 6 -c tessedit_char_whitelist=0123456789')

    def strToInt(self, str):
        # print("<--"+str)
        result = ""
        for s in str:
            if s in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                result = result + s
        # print("-->"+result)
        if len(result) == 0:
            return 0
        return int(result)

    def getTextByName(self, name):
        isObj, autoObject = self.getAutoObjectByName(name)
        if isObj:
            return self.getText(autoObject)
        else:
            return ""

    def clickToArea(self, autoObject):
        area1 = areaStrToList(autoObject.area1)
        x = int((area1[0] + area1[2]) / 2)
        y = int((area1[1] + area1[3]) / 2)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.5)

    def clickToAreaByName(self, name):
        isObj, autoObject = self.getAutoObjectByName(name)
        if isObj:
            self.clickToArea(autoObject)
