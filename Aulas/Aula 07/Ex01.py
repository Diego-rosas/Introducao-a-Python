notas = []
notas.append(float(input('Digite a nota 1: ')))
notas.append(float(input('Digite a nota 2: ')))
notas.append(float(input('Digite a nota 3: ')))
print('')

print('Nota 1: {}, Indice {} '.format(notas[0], notas.index(notas[0])))
print('Nota 2: {}, Indice {} '.format(notas[1], notas.index(notas[1])))
print('Nota 3: {}, Indice {} '.format(notas[2], notas.index(notas[2])))
print('')

soma = (notas[0] + notas[1] + notas[2])
media = soma/ len(notas)
print ('Media: {:.2f}'.format(media))
print('')

'''i = 0 
while i < len(notas[i]):
    list.append = float(input('Digite a nota1: '))
#N2 = int(input('Digite a nota2: '))
#N3 = int(input('Digite a nota3: '))
print(notas[0])'''
#notas = []
#notas.append= (N1)
