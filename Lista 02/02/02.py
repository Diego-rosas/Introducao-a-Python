#Questao 02
#Por: Diego Rosas

#o progrma faz um interrogatorio para classificar uma pessoa como suspeita ou nao de um crime
print('\n-----------------INTERROGATORIO CRIMINAL---------------------\n')
P1 = input('Telefonou para a vitima?[S/N]: ') #Variavel que recebe a primeira pergunta
P2 = input('Esteve no loca do crime?[S/N]: ') #Variavel que recebe a segunda pergunta
P3 = input('Mora perto da vitima?[S/N]: ')    #Variavel que recebe a terceira pergunta
P4 = input('Devia para a vitima?[S/N]: ')     #Variavel que recebe a quarta pergunta
P5 = input('Ja trabalhou com a vitima?[S/N]: ') #Variavel que recebe a quinta pergunta

contSim = 0                                     #inicia a variavel contSim que vai contar as respostas sim 
contNao = 0                                     #inicia a variavel contNao que vai contar as respostas nao
if P1.upper() == 'S':                           #verificacao da resposta da P1
    contSim += 1                                #acumulador para calcular o numero de resposta "sim"
     
if P2.upper() == 'S':                           #verificacao da resposta da P2
    contSim += 1                                #acumulador para calcular o numero de resposta "sim"

if P3.upper() == 'S':                           #verificacao da resposta da P3
    contSim += 1                                #acumulador para calcular o numero de resposta "sim"

if P4.upper() == 'S':                            #verificacao da resposta da P4
    contSim += 1                                #acumulador para calcular o numero de resposta "sim"

if P5.upper() == 'S':                            #verificacao da resposta da P5
    contSim += 1                                 #acumulador para calcular o numero de resposta "sim"
    

if contSim == 2:                                 #verifica se a quantidade de resposta sim eh igual a 2
    print('\nCLASSIFICACAO: Suspeita\n')         #Imprime a classificacao de suspeito que a pessoa se enquadra
elif contSim == 3 or contSim == 4:               #verifica se a quantidade de resposta sim eh igual a 3 ou 4
    print('\nCLASSIFICACAO: Cumplice\n')         #Imprime a classificacao de suspeito que a pessoa se enquadra
elif contSim == 5:                               #verifica se a quantidade de resposta sim eh igual a 5
    print('\nCLASSIFICACAO: Assassino\n')        #Imprime a classificacao de suspeito que a pessoa se enquadra
else:                                            #verifica se a quantidade de resposta sim não foi nenhuma das anteriores
    print('\nCLASSIFICACAO: Inocente\n')         #Imprime a classificacao de suspeito que a pessoa se enquadra
   