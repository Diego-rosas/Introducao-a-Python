import time
import os
#Questao 03
#Por: Diego Rosas
#Programa que simula um jogo da forca

# opcoes de jogadores
jogadores = {1:'Jogador que digita a palavra secreta.', 2:'Jogador que vai tentar adivinhar.'}
k = list(jogadores.keys())
v = list(jogadores.values())
# boas vindas
print('BEM VINDO AO JOGO DA FORCA!')
print('Qual jogador voce vai ser? ')
for i in range(len(jogadores)):
    print('{} - {}'.format(k[i],v[i]))
op = int(input('Opcao: '))
if op in jogadores:
    jogador = (jogadores[op])
# criar o input da palavra secreta
if op == 1:
    print('OK, voce escolheu a opcao {}: {}'.format(op,jogador))
    pl = input('Agora digite a palavra secreta: ')
else:
      print('OK, voce escolheu a opcao {}: {}'.format(op,jogador))  
      print('Aguarde a palavra secreta!')
# criar a contagem de tentativas
partesDoCorpo = {1:'Cabeça', 2:'Corpo', 3:'Braço Es', 4:'Braço Di', 5:'Perna Es', 6:'Perna Di'} # 6 tentativas ao todo
# receber as letras das tentativas e comparar com a palavra secreta
if pl != '':
    os.system('cls')
    print('Jogador 2 pode comecar!')
print('Voce tem {} tentativas!'.format(len(partesDoCorpo)))
for i in range(len(partesDoCorpo)):
    tentativa = input('{}ª tentativa: '.format(i + 1))
t = []
#print('\n')
for i in range(len(pl)):
    c = ('- ')
    t.append(c)
    print('{}'.format(c), end=' ')
print('')   
#print('  '.join(pl))
#print('\n',' '.join(c))    
# exibir o total de tentativas e as que restam
