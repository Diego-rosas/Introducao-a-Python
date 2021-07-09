import pyautogui
import pyperclip
import time
import emojis

pyautogui.PAUSE = 1
#abrir o navegador
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
#pyautogui.alert('Vai começar, aperte OK e não mexa em nada!')
#entrando no wpp web
time.sleep(1)
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('ctrl','f')
pyautogui.write('autonomos')
pyautogui.press('esc')
pyautogui.press('enter')
time.sleep(2)
mensagem = 'AI, A MELHOR SUBEQUIPE EM LINHA RETA!'
#'Bom dia, grupo! Essa msg esta sendo enviada como teste de automatização com python! EMERSON EH TOP!'
pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
pyautogui.write('KKKKKKKK pegou')
pyautogui.press('enter')