#Questao 10
#Por: Diego Rosas
#data: 21/07/2021
#Programa para manipular listas e dicionario

#Dicionario com os dados das pessoas 
pessoas = {'Joao': 26, 'Pedro': 50, 'Tiago': 35, 'Maria': 54, 'beatriz': 18, 'Fernanda': 25 }

pessoa_k = list(pessoas.keys())                  #Lista para receber as chaves(nomes) das pessoas
idades_v = list(pessoas.values())                #Lista para receber as valores(idades) das pessoas
pessoasM30 = []                                 #Lista para receber os nomes das pessoas acima de 30 anos
pessoasA30 = []                                 #Lista para receber os nomes das pessoas abaixo de 30 anos
#print(idades_v)

for i in range(len(pessoas)):                    #loop para percorrer o dicionario   
    if idades_v[i] > 30:                         #condicional para verificar as idades acima de 30 anos
        pessoasM30.append(pessoa_k[i])           #Passa para a lista os nomes das pessoas acima de 30 anos
    else:                                        #condicional para verificar as idades abaixo de 30 anos
        pessoasA30.append(pessoa_k[i])           #Passa para a lista os nomes das pessoas abaixo de 30 anos

print('Pessoas acima dos 30 anos: {}'.format(pessoasM30))  #Imprime a lista os nomes das pessoas acima de 30 anos
print('Pessoas abaixo dos 30 anos: {}'.format(pessoasA30))  #Imprime a lista os nomes das pessoas abaixo de 30 anos
print('')