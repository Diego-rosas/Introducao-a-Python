#Questao 05
#Por: Diego Rosas
#data: 19/07/2021
#Progrma para manipular arquivos

import os
import re

#abrir arquivo e copiar o conteudo
arquivo = open('05\lorem.txt')          #Abre o arquivo dentro da pasta 05
texto = arquivo.read()                  #Lê o arquivo e copia o conteudo como uma string para a variavel
#print(texto)
arquivo.close()                          #Fecha o arquivo
palavras_chaves = re.split('\s',texto)    #Pega as palavras separadas por um espaço '\s' e salva cada uma 
#print (palavras_chaves)                    #como um elemento em uma lista , no caso a palavras_chaves
qt_valor = []                              #cria uma lista vazia para receber os valores das quantidades
                                            #de palavras
for i in range(len(palavras_chaves)):       #Loop para percorrer a lista com as palavras
    y = palavras_chaves[i]                   #salva cada palavra na variavel y
    qt_valor.append(palavras_chaves.count(y))     #verifica a quantidade de cada palavra no texto e pega   
#print (qt_valor)                                 #o valor de quantas vezes ela se repete e salva 
                                                    #na lista quantidade valor 

dicionario = dict(zip(palavras_chaves,qt_valor))       #Faz um dicionario juntando a lista de palavras que eh passada como as chaves
                                                        #com a lista dos valores das quantidades de vezes que as palavras aparecem 
                                                        #que eh passado como os valores do dicionario

print('DICIONARIO:')                                    #imprime o titulo
print(dicionario)                                       #imprime o dicionario pronto