#Questao 10
#Por: Diego Rosas
#data: 18/07/2021
#Progrma que vai simular uma mini mega sena

import os
import time
import random


#Criando duas listas com valores de  0 - 9
list1 = list(range(0,10))
list2 = list(range(0,10))
embaralha_list1 = list1[0:len(list1)]
embaralha_list2 = list2[0:len(list2)]
sorteia_list1 = []
sorteia_list2 = []
dezenas1 = []
dezenas2 = []

#Embaralha as listas 
random.shuffle(embaralha_list1)
random.shuffle(embaralha_list2)

#sorteia um numero 5x das listas embaralhadas 1 e 2 
while True:
    print('='*45)                                   #começo do programa
    print('     SOTEIO DA MEGA SENA DA VIRADA!')
    print('='*45)
    for i in range(5):
        x = random.choice(embaralha_list1)
        y = random.choice(embaralha_list2)
        if x == y == 0:
            x = random.choice(embaralha_list1)
            y = random.choice(embaralha_list2)
        else:
            print('{}ª Dezena sorteada: {}{}'.format(i + 1,x,y))
        time.sleep(.5)
    sai = input('\nDeseja sortear de novo?[S/N]: ').upper()
    if sai == 'N':
        print('\n  FIM DO SORTEIO!')
        break
        
    os.system('cls')    
