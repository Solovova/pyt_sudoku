import numpy as np
import cv2
import pyscreenshot as ImageGrab 
import time

# pylint: disable=no-member

def draw_rect(event,x,y,flags,param):  
    getArea = param[0]
    if(event == cv2.EVENT_LBUTTONDOWN):  
        getArea.draw = True  
        getArea.rect[0], getArea.rect[1] = x, y
        getArea.rect[2], getArea.rect[3] = x, y
        getArea.drawRectangle()

    elif (event == cv2.EVENT_MOUSEMOVE):  
        if getArea.draw == True:
            getArea.rect[2], getArea.rect[3] = x, y
            getArea.drawRectangle()
    elif(event == cv2.EVENT_LBUTTONUP):  
        getArea.draw = False

class GetArea(object):
    rect = [0 ,0 ,100 ,100]
    draw = False

    def drawRectangle(self):
        self.img_out = self.img_orig.copy()
        cv2.rectangle(self.img_out,(self.rect[0],self.rect[1]),(self.rect[2],self.rect[3]),(0,0,255),2)
    
    def getArea(self,inRect):
        self.rect = inRect
        img_grab = ImageGrab.grab(bbox=(0, 0, 1919, 1079)) #x, y, w, h
        self.img_orig = cv2.cvtColor(np.array(img_grab), cv2.COLOR_RGB2BGR)
        self.drawRectangle()

        cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("image",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

        param = [self]
        cv2.setMouseCallback('image',draw_rect, param)  
        cv2.namedWindow('image')  

        while(True):
            cv2.imshow("image", self.img_out)
            time.sleep(0.1)
            key = cv2.waitKey(1)
            if key == 27:
                cv2.destroyAllWindows()
                return self.rect.copy()

# pylint: enable=no-member 