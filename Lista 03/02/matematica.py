#modulo para fazer as funcoes para calcular
#operacoes basicas
def soma(x,y):  #Funcao para realizar uma soma simples, de dois valores
	return (x + y)

def somaV ():	#Funcao para realizar uma soma complexa, de varios valores
	total = 0
	print('Digite os numeros que deseja Somar e 0 para sair: ')
	while True:
		num = float(input('+ '))
		total = total + num
		if num == 0:
			break
	if total%2 == 0 or total%2 == 1:
		print('Total = {} '.format(int(total)))
	else:
    		print('Total = {} '.format(total))
	
def subtracao (x,y):	 #Funcao de subtrair de apenas dois numeros
	return 	(x - y)

def multiplica (x,y):	#Funcao multiplicacao simples, de apenas dois valores
	return 	(x * y)

def multiplicaV():		#Funcao de mutiplicacao de varios numeros
        total = 1
        print('Digite os numeros que deseja mutiplicar e 1 para sair: ')
        while True:
            num = float(input('* '))
            total = total * num
            if num == 1:
                break
        if total%2 == 0 or total%2 == 1:
            print('Total = {} '.format(int(total)))
        else:
                print('Total = {} '.format(total))

def divisao (x,y):		#Funcao de divisao de apenas dois numeros
	return (x / y)	

#outras operacoes
def exponencial ():		#Funcao que calcula uma exponenciacao
	print('Digite os dois numeros que deseja calcular o Exponencial: ')
	x= int(input('Base: '))
	y= int(input('Expoente: '))
	return print('Total = {} '.format(x ** y))	

def fatorial():			#Funcao que calcula o fatorial de um numero
	print("Calculo do fatorial de um número!")
	n = int(input("Digite um numero inteiro nao-negativo: "))
	i     = 1  # contador
	n_fat = 1  
    # calcule n!
	while i <= n:
        	n_fat = n_fat * i 
        	i = i + 1
	print('{}! = {}'.format(n, n_fat)) 

#funcoes para calcular as areas  	
def areaTriangulo():	#Funcao que calcula a area de um Triangulo
	b = float(input('digite o valor da base[m]: '))
	h = float(input('digite o valor da altura[m]: '))
	return print('A area do Triangulo eh: {} m²'.format(divisao(multiplica(b,h),2)))

def areaQuadrado():		#Funcao que calcula a area de um Quadrado
	l = float(input('digite o valor do lado[m]: '))
	return print('A area do Quadrado eh: {} m²'.format(multiplica(l,l)))

def areaLosango():		#Funcao que calcula a area de um Losango
	D = float(input('digite o valor da Diagonal maior[m]: '))
	d = float(input('digite o valor da Diagonal menor[m]: '))
	return print('A area do Losango eh: {} m²'.format(divisao(multiplica(D,d),2)))

def areaRetangulo():	#Funcao que calcula a area de um Retangulo
	b = float(input('digite o valor da base[m]: '))
	h = float(input('digite o valor da altura[m]: '))
	return print('A area do Retangulo eh: {} m²'.format(multiplica(b,h)))

def areaTrapezio(): 	#Funcao que calcula a area de um Trpezio
	B = float(input('digite o valor da base maior[m]: '))
	b = float(input('digite o valor da base menor[m]: '))
	h = float(input('digite o valor da altura[m]: '))
	return print('A area do Trapezio eh: {} m²'.format(divisao(multiplica(soma(B,b),h),2)))

def areaCirculo():		#Funcao que calcula a area de um Circulo
	r = float(input('digite o valor do raio[m]: '))
	pi = 3.141592653589793
	return print('A area do Retangulo eh: {:.2f} m²'.format(multiplica(multiplica(r,r),pi)))
	
#Funcoes para calcular os volumes -- Ab = Area da base
def volumePiramide(): 		#Funcao para calcular o volume para piramides de base quadrada
	l = float(input('digite o valor da lado[m]: '))
	h = float(input('digite o valor da altura[m]: '))
	Ab = multiplica(l,l)
	return print('O Volume da Piramide eh: {} m³'.format(divisao(multiplica(Ab,h),3)))

def volumeCone():		#Funcao que calcula o volume de um Cone
	r = float(input('digite o valor do raio[m]: '))
	h = float(input('digite o valor da altura[m]: '))
	pi = 3.141592653589793
	Ab = multiplica(multiplica(r,r),pi)
	return print('O Volume do Cone eh: {:.2f} m³'.format(divisao(multiplica(Ab,h),3)))

def volumeCilindro():		#Funcao que calcula o volume de um Cilindro
	r = float(input('digite o valor do raio[m]: '))
	h = float(input('digite o valor da altura[m]: '))
	pi = 3.141592653589793
	Ab = multiplica(multiplica(r,r),pi)
	return print('O Volume do Cilindro eh: {:.2f} m³'.format(multiplica(Ab,h)))
	
def volumePrisma(): #Funcao que calcula o volume para prismas de base triangular
	Ab = float(input('digite o valor da area da base[m]: '))
	h = float(input('digite o valor da altura[m]: '))
	return print('O Volume do Prisma eh: {} m³'.format(multiplica(Ab,h)))

def volumeCubo():		#Funcao que calcula o volume de um Cubo
	l = float(input('digite o valor do lado[m]: '))
	return print('O Volume do Cubo eh: {} m³'.format(multiplica(multiplica(l,l),l))) #l ao cubo

def volumeEsfera():		#Funcao que calcula o volume de uma Esfera
	r = float(input('digite o valor do raio[m]: '))
	pi = 3.141592653589793
	rAoCubo = multiplica(multiplica(r,r),r)
	tresQuartos = divisao(4,3)
	return print('O Volume da Esfera eh: {:.2f} m³'.format(multiplica(multiplica(rAoCubo,pi),tresQuartos)))


def MDC():		#Funcao que calcula um MDC
	print('MDC entre dois numeros > 0!')
	n1 = int(input('  Digite o primeiro numero: '))	
	n2 = int(input('  Digite o segundo numero:  '))
	anterior = n1
	atual = n2
	resto = anterior % atual
	while resto != 0:
    		anterior = atual
    		atual = resto
    		resto = anterior % atual
	print('  O MDC entre {} e {} eh {}'.format(n1,n2,atual))

def MMC():		#Funcao que calcula um MMC
	print('MMC entre dois numeros > 0!')
	n1 = int(input('  Digite o primeiro numero: '))	
	n2 = int(input('  Digite o segundo numero:  '))
	if n1 > n2 and n1 % n2 == 0:
		mmc = n1
		print('  O MMC de {} e {} eh {}'.format(n1,n2,mmc))
	if n2 > n1 and n2 % n1 == 0:
		mmc = n2
		print('  O MMC de {} e {} eh {}'.format(n1,n2,mmc))
	if (n1 > n2 or n2 > n1) and n1 % n2 != 0:
		mmc = n1 * n2
		print('  O MMC de {} e {} eh {}'.format(n1,n2,mmc))
	else:
    		print(print('  O MMC entre {} e {} eh {}'.format(n1,n2,mmc))) 
	
	