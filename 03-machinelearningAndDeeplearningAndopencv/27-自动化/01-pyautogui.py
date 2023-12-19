import pyautogui
import time


while True:
    stop = int(input())
    print(stop)
    time.sleep(stop)
    pyautogui.moveTo((879, 252))
    pyautogui.click()