carros = {'A':1, 'B':2, 'C':3}

teste = list(carros)
print(teste)
modelos = list(carros.keys())
print('Temos os carros: {}, {}, {}'.format(modelos[0], modelos[1], modelos[2]))
consulta = input('Qual carro voce quer consultar o valor? ') #a variavel consulta vai receber um elemento como string
print('Esse carro custa: ', carros[consulta]) #o valor de consulta ja vai servir como a chave do dicionario

'''if consulta == 'A':
    print('Esse carro custa: ', carros['A'])

if consulta == 'B':
    print('Esse carro custa: ', carros['B'])

if consulta == 'C':
    print('Esse carro custa: ', carros['C'])'''