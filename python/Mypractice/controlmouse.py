import pyautogui
import time
import os


os.system("D:\\release\\release\\房源管理平台.exe")
from win32gui import IsWindowVisible
import win32gui
flag = True
while flag:
    time.sleep(3)
    wdname1=u"登录窗口"
    w1hd=win32gui.FindWindow(0,wdname1)
    print('current window is visible:',IsWindowVisible(w1hd))
    if w1hd != 0 and IsWindowVisible(w1hd):
        print('current window is visible:',IsWindowVisible(w1hd))
        flag = False

pyautogui.PAUSE=1.5
pyautogui.size()
#(1440,900)a123456a123456啊23456a123456
width,height=pyautogui.size()

#830 458
#移动到输入位置
pyautogui.moveTo(830, 458, duration=0.25)
#点击a123456
pyautogui.click(button='left')
pyautogui.typewrite('a123456')

#840 500
pyautogui.moveTo(840, 500, duration=0.25)
pyautogui.click(button='left')
