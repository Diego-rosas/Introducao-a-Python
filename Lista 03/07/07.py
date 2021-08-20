#Questao 07
#Por: Diego Rosas
#data: 21/07/2021
#Programa que para criar uma agenda telefonica

import os
import time

#cabecalio
print('='*30)
print('      Lista telefonica')
print('='*30)

#Menu de leitura/gravacao
print('O que voce deseja fazer? \n1 - Ler arquivo \n2 - Gravar arquivo')
op = int(input('Opcao: '))

#1- Leitura do arquivo

while True:
    if op == 1:
        agenda = open('07\\agenda.txt')
        conteudo = agenda.read()
        print(conteudo)
        agenda.close()
        break
    elif op == 2:
        agenda = open('07\\agenda.txt', 'a+')
        x = input('Digite: ') #se quiser que os nomes fiquem separados tem que dar espaco ou colocar visgula antes de digitar
        conteudo = agenda.write(x)
        agenda = open('07\\agenda.txt')
        conteudo = agenda.read()
        print(conteudo)
        agenda.close()
        break
    else:
        print('Opcao incorreta!')
        time.sleep(1)
        os.system('cls')  
        break
        