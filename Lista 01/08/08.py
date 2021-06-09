#Questao 05
#por: Diego Rosas

print('-------------------------------------------------------') #gambiarra para pular uma linha
info = input("Digite qualquer coisa: ") #Variavel que vai receber a informacao passada pelo usuario
print('')                                                          #gambiarra para pular uma linha
print(info,'eh um numeral? R:',info.isnumeric())                   #imprime a informacao, verifica se ela eh um numaral e retorna true/false
print(info,'eh um alfanumerico? R:',info.isalpha())                #imprime a informacao, verifica se ela eh um alfanumerico e retorna true/false
print(info,'esta todo em maiusculo? R:',info.isupper())            #imprime a informacao, verifica se ela esta todo em maiusculo e retorna true/false
print(info,'esta em braco? R:',info.isspace())                     #imprime a informacao, verifica se ela eh um espaço em branco e retorna true/false

print('-------------------------------------------------------') #gambiarra para pular uma linha