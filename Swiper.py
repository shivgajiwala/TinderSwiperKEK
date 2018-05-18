import os
import sys
import TinderConfig
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..\\lib\\PyAutoGUI-0.9.36')))
import pyautogui
import json
import time

class Swiper():    
    def __init__(self):
        '''Initialization'''
        with open ('SwiperConfig.json') as json_data_file:
            config = json.load(json_data_file).get("tinder")
        self.Emulator_Name = config.get("emulator")
        self.Emulator_Window = pyautogui.getWindow(self.Emulator_Name)
        self.X_Start_Offset = config.get("x_start_offset")
        self.Y_Start_Offset = config.get("y_start_offset")
        self.Start_Img_Name = config.get("start_img_name")
        self.Start_Pos = pyautogui.locateCenterOnScreen('tinderLogo.png')
        if (self.Emulator_Window == None or self.Start_Pos == None):
            raise Exception ('No Emulator Window Dectected!!!')
        
        
    def swipeLeft(self):
        pyautogui.moveRel(None,100)
        
    def swipeRight(self):
        pyautogui.dragRel(400, None, 0.3)

    def getEmulatorWindowName(self):
        return self.Emulator_Name

    def moveToStartPos(self):
        self.Start_Pos = pyautogui.locateCenterOnScreen('tinderLogo.png')
        pyautogui.moveTo(self.Start_Pos[0],self.Start_Pos[1])
        pyautogui.moveRel(self.X_Start_Offset,self.Y_Start_Offset)
        pyautogui.click (clicks=1)
    
if __name__ == '__main__':
    s = Swiper()
    while True:
        s.moveToStartPos()
        s.swipeRight();
        time.sleep(1)
