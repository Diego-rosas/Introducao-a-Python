#Questao 08
#Por: Diego Rosas
#Programa que simula uma fila de banco;
qtdPessoas = int(input('\nQuantos pessoas vc quer na fila? ')) #Variavel que recebe atraves de um input o valor da quantidade de pessoas que vai ter a fila;
pessoas = []                 #lista para receber os elementos relativos a quantidade digitada pelo usuaruio 

for i in range(1,qtdPessoas + 1):      #laco para fazero preenchimento da lista
    pessoas.append(i)                  #Metodo que adiciona um elemento popr vez na lista;
print('')                              #Pula uma linha 
print(*pessoas, sep=', ')                         #comando para caso queira imprimir a lista preenchida

for j in pessoas[::-1]:                #laco para fazer a retirada do elemento do inicio da fila;
   pessoas.pop(0)                      #metodo pararetirar os elementos de indice 0 da lista;
   print(*pessoas, sep=', ')                      #imprime a lista apos a retirada do elemento de indice zero(fila andando)

print('Acabou a fila!\n')               #mensagem de indicando o fim da fila e encerra o programa