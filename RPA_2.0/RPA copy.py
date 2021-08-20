

import pyautogui
import pyperclip
import time
meses = ['janeiro', 
        'fevereiro', 
        'março', 
        'abril', 
        'maio', 
        'junho', 
        'julho', 
        'agosto', 
        'setembro', 
        'outrubro', 
        'novembro', 
        'dezembro']
indiceMes = int(time.strftime('%m')) 
mesAtual = meses[indiceMes - 1] 
P1 = 'A3' #Primeira pessoa da tabela
P2 = 'A4'
P3 = 'A5'
P4 = 'A6'


pyautogui.PAUSE = 1
#procura e abre a tablela
pyautogui.press('winleft')
pyautogui.write('tabela Spotify atual')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(3)
#verifica se pessoa esta com o pagamento em dia ou não
pyautogui.hotkey('ctrl','l')
pyperclip.copy(mesAtual)
pyautogui.hotkey('ctrl','v')    #cola o valor da celular na caixa de texto do 'ir para'
pyautogui.press('enter')
pyautogui.press('esc')
time.sleep(1)
pyautogui.press('down')
pyautogui.hotkey('ctrl','c')    
confirmaPag = pyperclip.paste()
#print(confirmaPag)
if confirmaPag == 'x':
    statusPag = True #pagamento em dia
else:
    statusPag = False #pagamento atrasado
    #localiza e copia o nome da pessoa em atraso, depois fecha a pl
    pyautogui.hotkey('ctrl','g') #atalho de 'ir para'
    pyperclip.copy(P1)              #copia o valor da celular onde esta o nome da primeira pessoa
    pyautogui.hotkey('ctrl','v')    #cola o valor da celular na caixa de texto do 'ir para'
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl','c')    
    nome1 = pyperclip.paste()
    pyautogui.hotkey('alt','f4')
    time.sleep(1)
    #print(nome1)
#abrir o navegador
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
#entrando no wpp web
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
time.sleep(6)
#Pesquisa e localiza a pessoa em questao
pyautogui.hotkey('ctrl','f')
pyautogui.write(nome1)
pyautogui.press('esc')
pyautogui.press('enter')
time.sleep(2)

#Envia a mensagem de cobranca para a pessoa
mensagem = 'Olá, estou passando aqui para lhe informar que o pagamento do Spotify do mês atual está atrasado! Por favor entrar em contado comigo. Obrigado.'
pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
pyautogui.alert('Mensagem enviada! Fim da RPA aperte OK para encerrar')
pyautogui.hotkey('alt','f4')

#

