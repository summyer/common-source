import pyautogui
import time
import os


os.system("D:\\release\\release\\房源管理平台.exe")

time.sleep(7)

pyautogui.PAUSE=1.5
pyautogui.size()
#(1440,900)
width,height=pyautogui.size()

#830 458
#移动到输入位置
pyautogui.moveTo(830, 458, duration=0.25)
#点击
pyautogui.click(button='left')
pyautogui.typewrite('a123456')

#840 500
pyautogui.moveTo(840, 500, duration=0.25)
pyautogui.click(button='left')
