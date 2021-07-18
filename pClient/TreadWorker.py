import time
from PyQt5.QtCore import QThread, pyqtSignal  # pylint: disable=no-name-in-module, import-error
from engine import Engine
import pyautogui
from funArea import areaStrToList # pylint: disable=no-name-in-module, import-error

class TreadWorker(QThread):
    signal = pyqtSignal('PyQt_PyObject')
    loop = 0

    def __init__(self, window):
        QThread.__init__(self)
        self._isRunning = True
        self._isActive = False
        self.engine = Engine(window.listAutoObject)
        
    def run(self):
        
        # Sleep days 
        self.countSleepDays = 22
        self.countSleepDaysUseFood = False

        while self._isRunning:
            time.sleep(0.1)
            if self._isActive:
                self.workLoop_Fishing()
        

        # while self._isRunning:
        #     time.sleep(0.1)
        #     if self._isActive:
        #         self.sleepDays()
        
            
        # Work
        # while self._isRunning:
            # time.sleep(0.1)
            # if self._isActive:
            #     self.mainLoop()
                

    def stop(self):
        self._isRunning = False

    def changeState(self):
        self._isActive = not self._isActive

    def _commandGoToScreenMain(self):
        while not self.engine.isAreaByName("btnSleep"):
            self.engine.clickToAreaByName("btnFind")
            

    def _commandGoToScreenSearch(self):
        while not self.engine.isAreaByName("btnWoodHarvest"):
            self.engine.clickToAreaByName("btnFind")

    def _commandFES(self):
        food = self.engine.strToInt(self.engine.getTextByName("txtFood"))
        water = self.engine.strToInt(self.engine.getTextByName("txtWater"))
        energy = self.engine.strToInt(self.engine.getTextByName("txtEnergy"))

        print(str(food))
        print(str(water))
        print(str(energy))

        maxFood = 150
        maxWater = 125
        oneFood = 100
        oneWater = 35

        if (food<20):
            while True:
                self._commandGoToScreenMain()
                self.engine.clickToAreaByName("btnFood")
                food = self.engine.strToInt(self.engine.getTextByName("txtFood"))
                if (food > (maxFood - oneFood)):
                    break

        if (water<10):
            while True:
                self._commandGoToScreenMain()
                self.engine.clickToAreaByName("btnWater")
                water = self.engine.strToInt(self.engine.getTextByName("txtWater"))
                if (water > (maxWater - oneWater)):
                    break

        if (energy < 30):
            self._commandGoToScreenMain()
            self.engine.clickToAreaByName("btnSleep")
            self.engine.clickToAreaByName("bntSleepDoIt")
            time.sleep(8)

    def _commandHarvestMoveSlider(self):
        find, point = self.engine.getAreaCoordByName("btnHarverWoodSlider")
        if find:
            isObj, autoObject  = self.engine.getAutoObjectByName("btnHarverWoodSlider")
            if isObj:
                area2 = areaStrToList(autoObject.area2)
                moveFX = point[0] + area2[0]
                moveFY = point[1] + area2[1]
                pyautogui.moveTo(moveFX, moveFY)
                pyautogui.drag(area2[2] - moveFX, 0, 1, button='left')
                time.sleep(0.2)

    def _commandHarvest(self):
        self._commandGoToScreenSearch()
        self.engine.clickToAreaByName("btnWoodHarvest")
        if self.engine.isAreaByName("btnHands"):
            self._isActive = False
            return
        self._commandHarvestMoveSlider()
        self.engine.clickToAreaByName("btnWoodHarvestDoIt")
        time.sleep(1)
        while self.engine.isAreaByName("pbHarvestWood"):
            time.sleep(0.5)
    
    def _commandOven(self):
        self._commandGoToScreenSearch()
        self.engine.clickToAreaByName("btnOven")
        for i in range(10):
            self.engine.clickToAreaByName("btnOvenDoIt")


    def _commandSleepMoveSlider(self):
        find, point = self.engine.getAreaCoordByName("btnSleepSlider")
        
        if find:
            print("Sleep find: " + str(self.countSleepDays) + " Point0:" + str(point[0]) +  " Point1:" + str(point[1]) )
            isObj, autoObject  = self.engine.getAutoObjectByName("btnSleepSlider")
            if isObj:
                area2 = areaStrToList(autoObject.area2)
                moveFX = point[0] + area2[0]
                moveFY = point[1] + area2[1]
                pyautogui.moveTo(moveFX, moveFY)
                pyautogui.drag(area2[2] - moveFX, 0, 1, button='left')
                time.sleep(0.2)
        else:
            print("Sleep no find: " + str(self.countSleepDays))

    def sleepDays(self):
        self.countSleepDays =  self.countSleepDays - 1
        if (self.countSleepDays<0):
            self._isActive = False
            return

        self._commandGoToScreenMain()

        if (self.countSleepDaysUseFood):
            self.engine.clickToAreaByName("btnWater")
            self.countSleepDaysUseFood = False
        else:
            self.engine.clickToAreaByName("btnFood")
            self.countSleepDaysUseFood = True
        
        self.engine.clickToAreaByName("btnSleep")
        self._commandSleepMoveSlider()
        self.engine.clickToAreaByName("bntSleepDoIt")
        time.sleep(8)

    def _gotoFishScreen(self):
        print("goto Fish screen")
        if not self.engine.isAreaByName("fishBtnStart"):
            self.engine.clickToAreaByName("btnFind")
            self.engine.clickToAreaByName("fishBtnGoToFish")
        

    def _commandFishing(self):
        print("fishing")
        self.engine.clickToAreaByName("fishBtnStart")
        time.sleep(1)

    def mainLoop(self):
        print(self.loop)
        self.loop = self.loop + 1
        time.sleep(0.1)
        self._commandFES()
        self._commandFES()
        self._commandHarvest()
        # if self.loop % 10 == 0:
        #     self._commandOven()

    def workLoop_Fishing(self):
        print("Fish loop:" + str(self.loop))
        self.loop = self.loop + 1
        time.sleep(0.1)
        self._commandFES()
        self._commandFES()
        self._gotoFishScreen()
        self._commandFishing()

