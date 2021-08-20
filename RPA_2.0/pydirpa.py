#arquivo modulo das funcoes que vao ser usadas nmo programa de RPA
import pyautogui
import pyperclip
import time

#funcao para abrir navegadores, basta passar o parametro 'nomeNavegador' 
def abrenavegador (nomeNavegador): 
    pyautogui.press('winleft')
    pyautogui.write(nomeNavegador)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('win', 'up')
    time.sleep(1)
    pyautogui.hotkey('ctrl','t')
    time.sleep(1)

#funcao para abrir arquivos, basta passar o parametro 'nomeArquivo'
def abrearquivo (nomeArquivo):
    pyautogui.PAUSE = 1
    pyautogui.press('winleft')
    pyautogui.write(nomeArquivo)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(3)

#funcao para abrir o wpp e pesquisar as pessoas(pode ser qualquer pessoa na lista de contatos)
#basta escrever o nome de forma correta
def abrewpp (nomePessoa):
    linkwpp = 'https://web.whatsapp.com/'
    pyperclip.copy(linkwpp)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep(6)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl','alt','/')
    time.sleep(2)
    pyperclip.copy(nomePessoa)
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)


