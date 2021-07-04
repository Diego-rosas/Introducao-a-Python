#Questao 07
#Por: Diego Rosas
#Programa que simula uma pilha de pratos 

qtdPratos = int(input('\nQuantos pratos vc quer na pilha? ')) #Variavel que recebe atraves de um input o valor da quantidade de pratos;

pratos = []                                                  #lista para receber os elementos relativos a quantidade digitada pelo usuaruio 

for i in range(1,qtdPratos + 1):                            #laco para fazero preenchimento da lista 
    pratos.append(i)                                        #Metodo que adiciona um elemento popr vez na lista;

#print('\n',pratos)       -> comando para caso queira imprimir a lista preenchida                             

                                  
for j in range(qtdPratos,0, -1): #laco para contar a quantidade de vezes que deve ser impressa a lista
    #print(j)
   print(' ')                      #Pula uma linha 
   for x in range(j):               #laco para fazer a retirada do elemento do topo da pilha;
       print(pratos[x], end=' ')    #imprime os elementos da lista 

print('\nAcabaram os pratos!\n')      #mensagem final

#Metodo de fazer manipulando diretamente a lista
#for j in pratos[::-1]: 
#   pratos.pop()
#   print(pratos)