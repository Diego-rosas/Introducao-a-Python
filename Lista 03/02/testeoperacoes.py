#1º crie um modulo matematica
#2º crie funcoes paras as operacoes basicas
#3º faca um progama com diferentes operacoes basicas(calculo de area, volume, MDC)
#4º 

#3º- programa onde o usuario vai poder escolher a operacao que ele vai querer calcular
import matematica as mat
#menu de operações
operacoes = ['Area','Volume','MDC']
figuras = ['Triangulo','Quadrado','Losango','Retangulo','Trapezio','Circulo']
#figuras = {'Triangulo':['base','altura'], 'Quadrado':'lado', }
print('\nEscolha qual operacao voce deseja calcular!')
print('Digite um numero para escolher: \n1 - Area \n2 - Volume \n3 - MDC')

op = int(input('Opcao: '))
operacao = operacoes[op - 1]
#print(operacao)
#Menu das figuras para calcular a area  
if operacao == 'Area':
    print('\nEcolha qual figura voce vai querer calcular a {}:'.format(operacao))
    print('Digite um numero para escolher: \n1 - Triangulo \n2 - Quadrado \n3 - Losango \n4 - Retangulo \n5 - Trapezio \n6 - Circulo')
    op = int(input('Opcao: '))
    figura = figuras[op - 1]
    if figura == 'Triangulo':
        b = int(input('digite o valor da base[m]: '))
        h = int(input('digite o valor da altura[m]: '))
        print('A area do {} eh: {} m²'.format(figura,mat.divisao(mat.multiplica(b,h),2)))


