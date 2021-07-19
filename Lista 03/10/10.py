#Questao 10
#Por: Diego Rosas
#data: 18/07/2021
#Progrma que vai simular uma mini mega sena

import os
import time
import random

#Criando duas listas com valores de  0 - 9
list1 = list(range(0,10))                       #cria a lista 1 com numeros de 0-9
list2 = list(range(0,10))                       #cria a lista 1 com numeros de 0-9
embaralha_list1 = list1[0:len(list1)]           #copia a lista 1 para a lista embaralha
embaralha_list2 = list2[0:len(list2)]           #copia a lista 1 para a lista embaralha

#Embaralha as listas 
random.shuffle(embaralha_list1)                 #embaralha a lista 1   
random.shuffle(embaralha_list2)                 #embaralha a lista 2

#sorteia um numero 5x das listas embaralhadas 1 e 2 
while True:                                         #loop principal
    print('='*45)                                   #começo do programa
    print('     SOTEIO DA MEGA SENA DA VIRADA!')    #titulo
    print('='*45)
    for i in range(5):                            #loop para sortear os numeros das dezenas 
        x = random.choice(embaralha_list1)        #A variavel X vai receber o primeiro numero da dezena
        y = random.choice(embaralha_list2)        #A variavel y vai receber o segundo numero da dezena 
        if x == y == 0:                            #Analisa se tera uma dezena '00'; 
            x = random.choice(embaralha_list1)      #Se for sorteado um '00' repete o sorteio
            y = random.choice(embaralha_list2)
        else:                                       #senao for sorteado uma dezena 00
            print('{}ª Dezena sorteada: {}{}'.format(i + 1,x,y)) #segue para imprimir as dezenas sorteadas
        time.sleep(.5)                                          #pausa de meio segundo entre as impressoes
    sai = input('\nDeseja sortear de novo?[S/N]: ').upper()  #pergunta se quer sortear de novo
    if sai == 'N':                                   #Se a resposta for sim limpa a tela e comeca de novo
        print('\n  FIM DO SORTEIO!')                 #Sea resposta for nao, imprime a msg   
        break                                        #encerra o programa 
        
    os.system('cls')                                 #limpa a tela para fazer outro sorteio 
