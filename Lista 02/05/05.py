#Questão 05
#Por: Diego Rosas
#Programa que pergunta quantos numero primos ele quer ver e mostra aquela determinada quantidade dentro de um 
#range de 1 ate 200.
print('\n----------------------------CALCULADORA DE NUMEROS PRIMOS -----------------------------------') #titulo ficiticio
while True:                                                                 #Laco para repetir o programa todo quantas vezes o usuario desejar
    xprimos = int(input('\nDigite quantos numeros primo voce que ver entre 1 e 200: ')) #variavel que recebe a quantidade de primos que deseja ver
    numeros = list(range(1,201))                                            #cria a lista e preenche com os 200 numeros intieros 
    primos = []                                                             #cria a lista vazia, que vai receber os numeros primos 

    i = 0                                                 #iniciacao da variavel para usar no laco for                                               
    for i in range(1, len(numeros) + 1):                  #Laco for que vai criar uma contagem com o range igual ao valor do maior indice da lista numeros
        cont = 0                                          #Variavel para contar a quantidade 
        for j in range(1, i + 1):                         #Laco que vai fazer a segunda contagem dos numeros                   
            if(i % j == 0):                               #condicional que verifica se os numeros vao ser divisiveis   
                cont += 1                                 #acumulador para caso um numero seja divisivel 
        if (cont == 2):                                   #condicional que pega os numeros que foram divididos 2x e grava na lista primos
            primos.append(i)                              #adiciona os numeros primos na lista
            
    print('\n Os {} numeros primos sao: {}'.format(xprimos,primos[0:xprimos]))      #imprime somente a quantidade de numeros primos solicitada  

    resposta = input('\nDeseja continuar?[S/N]: ')          #pergunta de verificacao para continuar a rodar o programa 
    if resposta.upper() != 'S':                             #compara a resposta para acionar o break    
        print('\n  FIM!\n')                                 #imprime um aviso de fim do programa 
        break                                               #Para o programa
            
