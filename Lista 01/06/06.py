#Questao 06
#Por: Diego Rosas

print('-----------------------------------------------------------------------') #gambiarra para pular uma linha
diasDaSemana = ['domingo','segunda','terça','quarta','quinta','sexta','sabado'] #Array com os dias da semana com indeices de 0 até 6

diaMes = int(input("Qual dia do mês voce vai sair de ferias?[0 á 31]: ")) #Variavel que vai guardar o dia do mes que sera informado pelo usuario 
diaSemana = input("Qual dia da semana voce vai sair de ferias?[domingo á sabado]: ") #Variavel que vai guardar o dia da semana que sera informado pelo usuario 
qtdDias = int(input("Quantos dias voce vai ficar de ferias?: ")) #Variavel que vai guardar a quantidade de dias que o usuario dicara de ferias 

i = 0    #Variavel que vai guardar os indices dos dias da semana
a = 0    #Variavel para ser feita a condicao logica do while   
while(a==0):                            #Estrutura de repeticao que vai fazer a varredura do array diasDaSemana
    if diasDaSemana[i] == diaSemana:    #Estrutura condicional para comparar o conteudo do array com o dia da semana informado prlo usuario
        a = 1                           #variavel para fazer a logica de parada do while
    else:                               #Estrutura condicional que vai habilitar o contador do while
        i = i + 1                       #contador 

diaVolta = qtdDias % 7                  #variavel que vai guardar o resto da divisao, dos dias que o usuario vai ficar de ferias, por 7.
                                        #essa logica nos permite isolar a quantidades de dias que vai ser usado para saber dia da semana que ele vai voltar ao trabalho
diaSemanaVolta = diaVolta + i           #variavel que vai guardar o indice do dia da semana que o usuario vai voltar ao trabalho
                                         
print('')                               #gambiarra para pular uma linha
print('Você voltará a trabalhar na', diasDaSemana[diaSemanaVolta]) #Imprime a string correspondente ao numero passado(diaSemanaVolta)
print('----------------------------------------------------------------------') #gambiarra para pular uma linha

#A logica usada: para o cauculo ficar mais preciso usei o valor 7 que eh o numero de dias numa semana, ja que essa informação
#nao varia(uma semana sempre vai ter 7 dias independente do mes) diferentementos da quantidade de dias de um mes;
#Qualquer qtdDias que for passado ao ser dividido por 7 vai retornar um resto que serah usado para calcular o dia da volta;

#Partindo desse ponto o calculo vai ficar assim: O resto de qtDias % 7 sempre vai ser menor que 7, logo

#Exemplo do calculo
#diaDaSemana = segunda (indice = 1, no array)
#qtdDias = 7, 7/7 = 1 e resto = 0
#logo se ele saiu de ferias numa segunda e tirou 7 dias, apenas, devera voltar na proxima segunda.
# 1(indice da segunda) + 0(resto da divisao; 0 = domingo no array) = 1 que tambem uma segunda no array(dia de volta ao trabalho).

#Ex. 02
#diaDaSemana = quarta (indice = 3 = i)
#qtdDias = 30;  30 % 7 = 2
#diaVolta = 2
#diaSemanaVolta = diaVolta + i
#diaSemanaVolta = 3 = (quarta no array)
# diasDaSemana[diaSemanaVolta] - retorna a string 'quarta' do array. 

#supondo que o usuario trabalhe de segunda a sexta, e ele irah informar um desses dias, o resultado sempre irah cair em um desses dias.