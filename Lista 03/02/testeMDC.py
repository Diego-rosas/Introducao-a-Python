def subtracao ():
	total = 0
	atual = 0
	print('Digite os numeros que deseja subtrair e 0 para sair: ')
	while True:
		num = float(input(' '))
		anterior = num
		atual = anterior 
		''' if anterior > atual:
			total = anterior - atual '''
		if num == 0:
			break
	print(num)
	print(anterior)
	print(atual)
	print('Total = {} '.format(total))
	''' if total%2 == 0 or total%2 == 1:
		print('Total = {} '.format(int(total)))
	else:
    		print('Total = {} '.format(total)) '''

subtracao()

