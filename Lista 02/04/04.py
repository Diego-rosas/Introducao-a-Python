#Questao 04
#Por: Diego Rosas
#Programa para fazer manipulacoes com listas

L1 = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P'] #Lista 1 com 15 elementos
L2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]            #Lista 2 com 15 elementos

L3 = []                                 #Lista 3 sendo criada vazia para receber os elementos da L1 e L2
L3 = L1[1:len(L1):2] + L2[1:len(L2):2]     #Fromula que copia os elementos de indice impar da L1 e L2, faz uma soma entre elas
print('')                                  #e depois cola na L3

print('\nLista 1 tem {} elementos.'.format(len(L1))) #imprime a quantidade de elementos da L1
print(L1)                                            #imprime os elementos da L1   

print('\nLista 2 tem {} elementos.'.format(len(L2))) #imprime a quantidade de elementos da L2
print(L2)                                            #imprime os elementos da L1

print('\nLista 3 tem {} elementos.'.format(len(L3))) #imprime a quantidade de elementos da L3
print(L3,'\n')                                       #imprime os elementos da L1

#outra forma de se fazer:   
#i=0
#for i in range(len(L1)):     
#    if(i%2 != 0):
#        L3.insert(i,L1[i])
#        L3.insert(i,L2[i])
#Resutado -> ['B', 2, 'D', 4, 'F', 6, 'H', 8, 'J', 10, 'M', 12, 'O', 14]
