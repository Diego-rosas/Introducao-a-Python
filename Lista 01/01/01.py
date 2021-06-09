#Questão 01
#Por: Diego Rosas

print("--------------CALCULADORA DE SEGUNDOS---------------------") #titulo inventado para o programa
qtDias = int(input("Digite uma quantidade de dias: ")) #variavel que grava a quantidade de dias recebida pela entrada
qtHoras = int(input("Digite uma quantidade de horas: ")) #variavel que grava a quantidade de horas recebida pela entrada
qtMinutos = int(input("Digite uma quantidade de minutos: ")) #variavel que grava a quantidade de minutos recebida pela entrada
qtSegundos = int(input("Digite uma quantidade de segundos: ")) #variavel que grava a quantidade de segundos recebida pela entrada

diasParaSegundos = qtDias * 86400 #Variavel que grava o calculo da quantidade de dias para segundos
hrsParaSegundos = qtHoras * 3600  #Variavel que grava o calculo da quantidade de horas para segundos
minParaSegundos = qtMinutos * 60  #Variavel que grava o calculo da quantidade de minutos para segundos

#Variavel que grava a soma total dos segundos 
totalSegundos = diasParaSegundos + hrsParaSegundos + minParaSegundos + qtSegundos
print("")                                               #gambiarra para pular uma linha
print("O tempo total em segundos é: ", totalSegundos)   #imprimindo o resulto final
print("")                                               #gambiarra para pular uma linha