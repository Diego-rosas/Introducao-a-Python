#Questao 06
#Por: Diego Rosas
#Programa para fazar um cadastro de pessoas e suas caracteristicas usando variaveis 
dados = []
nomes = []
pesos = []
alturas = []
IMCs = []
c = 0
print('Digite os dados dos alunos para fazer o cadastro:')
while True: 
    while True:                         #laco do cadastro de alunos
        c += 1
        nome = input('\nDigite o nome do {}º aluno: '.format(c))
        nomes.append(nome)               #salva so os nomes na lista nomes
        dados.append(nome)               #salva so os nomes na lista dados
        dados.append(int(input('Digite a idade: ')))
        peso = (float(input('Digite o peso em kg : ')))
        pesos.append(peso)
        dados.append(peso)
        altura = (float(input('Digite a altura: ')))
        alturas.append(altura)            
        dados.append(altura)    
        calculaIMC = peso / (altura * altura)
        IMCs.append(round(calculaIMC))
        saiCadastro = input('\ndeseja continuar? [s/n]: ')      #variavel para sair do laco do cadastro
        if saiCadastro == 'n':
            print('\nTotal de pessoas cadastradas: ',c)
            break
    while True:                             #laco para fazer a consulta do imc
        fazPesq = input('\nDeseja consultar o IMC?[S/N]: ')
        if fazPesq.upper() == 'S':
            pesq = input('\nDigite um nome para consultar o IMC: ')
            if pesq in dados:
                indiceNome = dados.index(pesq)
                IMC = IMCs[indiceNome]
                print('IMC: {:.2f}'.format(IMC))
            if IMC > 30:
                print('O aluno(a) esta Obeso!')
            else:
                print('O aluno(a) nao esta Obeso!')
        else:
            break
        saiPesq = input('\nDeseja fazer uma nova consulta?[s/n]: ')  #variavel para sair do laco da consulta
        if saiPesq == 'n':
            break

    saiProg = input('\nDeseja continuar o cadastro? [s/n]: ') #variavel para sair do laco do programa
    if saiProg == 'n':
        break
#Impessao das informacoes dos alunos que forem cadastrados
print('\nNomes: ',nomes)
print('Pesos: ',pesos)
print('Altura: ',alturas)
print('IMCs: ',IMCs)
print('Lista com tadas informacoes dos alunos:\n',dados)

#Dados pre cadastrados para uso nas letras b) e c)
dadosGerais = ['jose', 60, 90.0, 1.80, 'bia', 25, 60.0, 1.60, 'mateus', 30, 80.0, 1.65, 'cristina', 40, 70.0, 1.70, 'ricardo', 45, 55.0, 1.70]

#letra b): imprime a lista com os nomes ordenados retirados de dadosGerais[];
print('\nNomes em ordem alfabetica: ',sorted(dadosGerais[0:len(dadosGerais):4])) 

#letra c)
nomesG = list(dadosGerais[0:len(dadosGerais):4])
pesosG = list(dadosGerais[2:len(dadosGerais):4])
alturasG = list(dadosGerais[3:len(dadosGerais):4])
maiorPeso = max(pesosG)
menorPeso = min(pesosG) 

if maiorPeso in pesosG:
   indiceNomeMaiorP = pesosG.index(maiorPeso)
   nomeMaiorPeso = nomesG[indiceNomeMaiorP]
   alturaMaiorP = alturasG[indiceNomeMaiorP]

if menorPeso in pesosG:
    indiceNomeMenorP = pesosG.index(menorPeso)
    nomeMenorPeso = nomesG[indiceNomeMenorP]
    alturaMenorP = alturasG[indiceNomeMenorP]

imcMaiorP = maiorPeso / (alturaMaiorP * alturaMaiorP)
imcMenorP = menorPeso / (alturaMenorP * alturaMenorP)

#print('\nMaior IMC: ',imcMaiorP)
#print('Menor IMC: ',imcMenorP)

print('\nNomesG: ',nomesG)
print('PesosG: ',pesosG)
print('AlturasG: ',alturasG)

print('\nO aluno mais pesado eh {} e o IMC dele eh {:.2f}!'.format(nomeMaiorPeso,imcMaiorP))
print('O aluno mais leve eh {} e o IMC dele eh {:.2f}!\n'.format(nomeMenorPeso,imcMenorP))
#print('\nMenor peso: ',min(dadosGerais[2:len(dadosGerais):4]))

#OBS.: Professora resolvi usar listas para fazer esse exercicio, mas sei que poderia ter feito algumas partes com dicionario, ou ele todo,
#porem a principio achei que a logica do algoritmo ficou mais facil de desenvolver usando esse metodo;


