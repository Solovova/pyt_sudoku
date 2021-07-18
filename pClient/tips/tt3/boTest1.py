import cv2
import time
import numpy as np
import pyscreenshot as ImageGrab
import pyautogui
import time

x1 = 650
y1 = 20
x2 = 1220
y2 = 950

def find_patt(image, patt, thres):
    img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (patt_H, patt_W) = patt.shape[:2]
    res = cv2.matchTemplate(img_grey, patt, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res > thres)
    return patt_H, patt_W, zip(*loc[::-1])

def click_on_btnname(btnName, img):
    patt = cv2.imread(btnName, 0)
    h, w, points = find_patt(img, patt, 0.60)
    pointsl = list(points)
    if len(pointsl) != 0:
        pyautogui.moveTo(pointsl[0][0]+w/2+x1, pointsl[0][1]+h/2+y1)
        pyautogui.click()
        return True
    return False

def read_img():
    screenshot = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    img = np.array(screenshot.getdata(), dtype='uint8').reshape(
            (screenshot.size[1], screenshot.size[0], 3))
    return img



if __name__ == '__main__':
    ite = 0
    while(True):
        ite = ite +1
        print (ite)
        img = read_img()
        click_on_btnname('butt01.png', img)
        click_on_btnname('butt02.png', img)
        click_on_btnname('butt03.png', img)
        click_on_btnname('butt04.png', img)
        click_on_btnname('Mis01.png', img)
        click_on_btnname('Mis02.png', img)
        click_on_btnname('buttNoReclam.png', img)
        # if click_on_btnname('buttRecl01.png', img):
        #     time.sleep(32)
        #     img = read_img()
        #     click_on_btnname('buttRecl02.png',img)
        #     click_on_btnname('buttRecl03.png',img)
        #     click_on_btnname('buttRecl04.png',img)

