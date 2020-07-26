import pyautogui, sys
import pygetwindow as gw
import re
import input as i
import time

from pynput.keyboard import Key, Controller

VK_RETURN = 0x1C              # ENTER key
KEY_A = 0x41

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
#######################################################################################################################

pyautogui.FAILSAFE = True #Moving mouse to top left of screen will abort execution
pyautogui.PAUSE = 1 #Seconds to wait between each pyautogui API call

screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2) #Move to middle of screen each loop

#Ensure Black Desert Window is active window
r = re.compile("BLACK DESERT.*")
windowList = gw.getAllTitles()
bdo = list(filter(r.match, windowList))[0]
gw.getWindowsWithTitle(bdo)[0].activate()
time.sleep(1)
# keyboard = Controller()
# keyboard.press(Key.enter)
# time.sleep(0.2)
# keyboard.release(Key.enter)


i.SendInput(i.Keyboard(VK_RETURN))
time.sleep(0.2)
i.SendInput(i.Keyboard(VK_RETURN, KEYEVENTF_KEYUP))
time.sleep(0.2)
i.SendInput(i.Keyboard(KEY_H))
time.sleep(0.2)
i.SendInput(i.Keyboard(KEY_H, KEYEVENTF_KEYUP))


