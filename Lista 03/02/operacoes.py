#1º crie um modulo matematica
#2º crie funcoes paras as operacoes basicas
#3º faca um progama com diferentes operacoes basicas(calculo de area, volume, MDC)
#4º 

#3º- programa onde o usuario vai poder escolher a operacao que ele vai querer calcular
import matematica as mat
import time
import os

operacoes = {1:'Area', 2:'Volume', 3:'MDC', 4:'MMC', 5:'soma', 6:'somaV', 7:'subtracao',            #Dicionario com todas as operacoes disponiveis 
             8:'multiplicacao',9:'multiplicacaoV', 10:'divisao', 11:'exponencial', 12:'fatorial'}
k = list(operacoes.keys())                  #Lista para receber as chaves das oeracoes
v = list(operacoes.values())                #Lista para receber os valores das oeracoes

figuras = ['Triangulo','Quadrado','Losango','Retangulo','Trapezio','Circulo']       #lista do menu das figuras para calcular a area
figurasV = ['Piramide','Cone','Cilindro','Prisma','Cubo','Esfera']                  #lista do menu das figuras para calcular o volume
while True:                                                             #Loop do programa geral
    #menu de operações
    print('Escolha qual operacao voce deseja calcular:')                
    for i in range(len(operacoes)):                                     #Loop para imprimir o menu de operacoes disponiveis
        print('{} - {}'.format(k[i],v[i]))                              #Imprime as operacoes disponiveis
    op = int(input('Opcao: '))                                          #recebe a opcao de operaca escolhida pelo usuario
    if op in operacoes:                                                 #verifica se a opcao esta entre as operacoes disponiveis
        operacao = (operacoes[op])
    
    if operacao == 'Area':      #Menu das figuras para calcular a area  
        print('\nEcolha qual figura voce vai querer calcular a {}:'.format(operacao))
        print('1 - Triangulo \n2 - Quadrado \n3 - Losango \n4 - Retangulo \n5 - Trapezio \n6 - Circulo')
        op = int(input('Opcao: '))                          #recebe a opcao escolhida pelo usuario
        figura = figuras[op - 1]
        if operacao == 'Area' and figura == 'Triangulo':    #Operacao que calcula a area de um Triangulo
            mat.areaTriangulo()
        if operacao == 'Area' and figura == 'Quadrado':     #Operacao que calcula a area de um Quadrado
            mat.areaQuadrado()   
        if operacao == 'Area' and figura == 'Losango':      #Operacao que calcula a area de um Losango
            mat.areaLosango()
        if operacao == 'Area' and figura == 'Retangulo':    #Operacao que calcula a area de um Retangulo
            mat.areaRetangulo()
        if operacao == 'Area' and figura == 'Trapezio':     #Operacao que calcula a area de um Trpezio
            mat.areaTrapezio()
        if operacao == 'Area' and figura == 'Circulo':      #Operacao que calcula a area de um Circulo
            mat.areaCirculo()
    if operacao == 'Volume':    #Menu das figuras para calcular o volume 
        print('\nEcolha qual figura voce vai querer calcular o {}:'.format(operacao))
        print('1 - Piramide \n2 - Cone \n3 - Cilindro \n4 - Prisma \n5 - Cubo \n6 - Esfera')
        op = int(input('Opcao: '))                  #recebe a opcao escolhida pelo usuario
        figura = figurasV[op - 1]
        if operacao == 'Volume' and figura == 'Piramide':   #Operacao que calcula o volume de uma Piramide
            mat.volumePiramide()
        if operacao == 'Volume' and figura == 'Cone':       #Operacao que calcula o volume de um Cone     
            mat.volumeCone()
        if operacao == 'Volume' and figura == 'Cilindro':   #Operacao que calcula o volume de um Cilindro
            mat.volumeCilindro()
        if operacao == 'Volume' and figura == 'Prisma':     #Operacao que calcula o volume de um Prisma
            mat.volumePrisma()
        if operacao == 'Volume' and figura == 'Cubo':       #Operacao que calcula o volume de um cubo
            mat.volumeCubo()
        if operacao == 'Volume' and figura == 'Esfera':     #Operacao que calcula o volume de uma Esfera
            mat.volumeEsfera()
    if operacao == 'MDC':       #Operacao que realiza um MDC
        mat.MDC()
    if operacao == 'MMC':       #Operacao que realiza um MMC
        mat.MMC()
    if operacao == 'soma':      #Operacao soma simples, de dois valores
        print('Digite os dois numeros que deseja Somar: ')
        x= int(input('digite um numero: '))
        y= int(input('digite um numero: '))      #operacao de soma de apenas dois numeros
        mat.soma(x,y)
        print('Total = {} '.format(x + y))	
    if operacao == 'somaV':      #operacao de soma de varios numeros
        mat.somaV()
    if operacao == 'subtracao':  #operacao de subtrair de apenas dois numeros
        print('Digite os dois numeros que deseja Subtrair: ')
        x= int(input('digite um numero: '))
        y= int(input('digite um numero: '))    
        mat.subtracao(x,y)
        print('Total = {} '.format(x - y))
    if operacao == 'multiplicacao':  #Operacao multiplicacao simples, de apenas dois valores
        print('Digite os dois numeros que deseja Mutiplicar: ')
        x= int(input('digite um numero: '))
        y= int(input('digite um numero: '))  #operacao de mutiplicacao de apenas dois numeros
        mat.multiplica(x,y)
        print('Total = {} '.format(x * y))
    if operacao == 'multiplicacaoV':   #operacao de mutiplicacao de varios numeros
        mat.multiplicaV()
    if operacao == 'divisao':          #operacao de divisao de apenas dois numeros
        print('Digite os dois numeros que deseja Dividir: ')
        x= int(input('digite um numero: '))
        y= int(input('digite um numero: '))    
        mat.divisao(x,y)
        print('Total = {} '.format(x / y))
    if operacao == 'exponencial':   #operacao de exponenciacao
        mat.exponencial()
    if operacao == 'fatorial':   #operacao que calcula o fatorial
        mat.fatorial()
    
    sai = input('Quer calcular de novo?[S/N]: ')    #Pergunta se o usuario quer fazer outra conta
    if sai.upper() == 'S':                            #verifica a resposta
        os.system('cls')                              #limpa a tela
    else:
        break                                          #Caso a resposta seja 'N', para o programa
    


