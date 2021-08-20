import time
import os
#Questao 03
#Por: Diego Rosas
#Programa que simula um jogo da forca

# opcoes de jogadores
jogadores = {1:'Jogador que digita a palavra secreta.', 2:'Jogador que vai tentar adivinhar.'}
k = list(jogadores.keys())
v = list(jogadores.values())
palavra_secreta = []
letras_descobertas = []
# boas vindas
print('BEM VINDO AO JOGO DA FORCA!')

#Pergunta qual jogador cada pessoa vai ser
print('Qual jogador voce vai ser? ')
for i in range(len(jogadores)):
    print('{} - {}'.format(k[i],v[i]))
op = int(input('Opcao: '))
if op in jogadores:
    jogador = (jogadores[op])

#verifica a escolha dos jogadores e criar o input da palavra secreta
vez = True
while vez == True:
    if op == 2:
        print('OK, voce escolheu a opcao {}: {}'.format(op,jogador))  
        print('Aguarde a palavra secreta!')
        vez = False
        #print('OK, voce escolheu a opcao {}: {}'.format(op,jogador))
        pl = input('\nJogador 1 digite a palavra secreta: ')
    elif op == 1:
        print('OK, voce escolheu a opcao {}: {}'.format(op,jogador))
        pl = input('Digite a palavra secreta: ')
        break
    

# receber as letras das tentativas e comparar com a palavra secreta
#pl = ''
tentativas = 6
if pl != '':
    for i in range(len(pl)):
        palavra_secreta.append(pl[i])
    for j in range(0, len(palavra_secreta)):
        letras_descobertas.append('-')
    os.system('cls')
    print('Jogador 2 pode comecar!')
print('Voce tem {} tentativas!'.format(tentativas)) 

acertou = False
while acertou == False:
    letra = str(input('\nDigite a letra: '))
    print('')
    for i in range(0, len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            letras_descobertas[i] = letra

        print(letras_descobertas[i], end=' ')

        """ if letra != palavra_secreta[i]:
            parte = partesDoCorpo[i]
            print(parte) """

    acertou = True
    print('')
    for x in range(0, len(letras_descobertas)):
        if letras_descobertas[x] == '-':
            acertou = False
# exibir o total de tentativas e as que restam
