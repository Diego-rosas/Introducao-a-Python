#C:\Users\Diego\Google Drive (ufpebackup@gmail.com)\UFPE\2020.2\INTRODUÇÃO A PYTHON EM ENGENHARIA\Introducao-a-Python\RPA_2.0
import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press('winleft')
pyautogui.write('tabela Spotify atual')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(3)