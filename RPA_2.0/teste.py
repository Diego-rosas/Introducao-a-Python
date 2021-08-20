import time

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outrubro', 'novembro', 'dezembro']

indiceMes = int(time.strftime('%m')) 

mesAtual = meses[indiceMes - 1] 

print(mesAtual)

#dias = list(range(1,32))
#print(dias)
#diaAtual = int(time.strftime('%d'))
diaAtual = 10
#print(diaAtual)
if diaAtual < 8:
    print('O aluguel ainda nao venceu.')
elif diaAtual == 8:
    print('O aluguel vence hoje.')
else:
    print('O aluguel esta vencido!')