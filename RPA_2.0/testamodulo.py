import pydirpa as dirpa
import pyautogui
import time

dirpa.abrenavegador('chrome') #chrome e Edge: ok | Firefox: erro na hora de pesquisar o contato

dirpa.abrewpp('pessoa1')

pyautogui.write('teste')
pyautogui.press('enter')
#dirpa.abrearquivo('cobra')