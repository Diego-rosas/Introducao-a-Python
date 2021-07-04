#Questão 03
#Por: Diego Rosas

#Programa para comparar o consumo de alguns modelos de carros e dizer qual o mais economico.

carros = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] #lista de 'modelo' de carros
consumo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                   #lista do 'consumo' dos carros em KM/L

#letra a)
Economico = max(consumo)                                #variavel que recebe o valor do maior consumo da lista de consumos
if Economico == max(consumo):      
    indiceCarro = consumo.index(max(consumo))
    print('Carro: ',carros[indiceCarro], 'dfafafaf') 

#letra b) e c)
i=0
km = int(input('Digite uma quantidade de KM: '))
for i in range(len(consumo)):
    litros = km / consumo[i] #calculo da letra b)
    gasto = litros * 5.5    #calculo da letra c)
    print('Com o carro {} rodando {} km vai consumir {:.2f}L e vai gastar R$ {:.2f} !'.format(carros[i], km, litros, gasto))

