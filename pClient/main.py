import logging

from PyQt5 import QtWidgets
import sys
import keyboard

from pClient.guiApp import GuiApp


def hetKeySF1(window):
    print("SF1")
    window.treadWorker.changeState()
    
def main():
    logging.basicConfig(level=logging.DEBUG)
    app = QtWidgets.QApplication(sys.argv)  
    window = GuiApp() 
    keyboard.add_hotkey('shift+F1', hetKeySF1, args=(window, ), suppress=True, trigger_on_release=True)
    window.show()  
    app.exec_()  

    window.saveList()
    keyboard.clear_all_hotkeys()
    window.treadWorker.stop()

if __name__ == '__main__':  
    main()  