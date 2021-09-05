import pyautogui
import time

time.sleep(5)
pyautogui.write('127.0.0.1', interval=0.25)
pyautogui.press('enter')   

pyautogui.write('admin', interval=0.25)
pyautogui.press('enter') 
pyautogui.write('admin', interval=0.25)
pyautogui.press('enter')   
    
pyautogui.write('1', interval=0.25)
pyautogui.press('enter')   
time.sleep(5)
pyautogui.write('0', interval=0.25)
pyautogui.press('enter')   