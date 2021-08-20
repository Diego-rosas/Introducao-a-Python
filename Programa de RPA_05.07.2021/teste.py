import time

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outrubro', 'novembro', 'dezembro']

indiceMes = int(time.strftime('%m')) 

mesAtual = meses[indiceMes - 1] 

print(mesAtual)