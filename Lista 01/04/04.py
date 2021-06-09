#Questao 04
#por: Diego Rosas

print('-------------------------------------------------------') #gambiarra para pular uma linha
valorHora = int(input('Quanto voce ganha por hora[R$]? ')) #Variavel que recebe o valor da hora trabalhada 
print('[1 dia de trabalho = 8hrs | 1 mês = 160hrs]')          #informação complementar para ajudar o usuario no calculo das horas trabalhadas
qtdHoras = int(input('Quantas horas voce trabalhou no mes? ')) #Variavel que recebe o total de horas trabalhadas no mes
 
salarioBrutoTotal = qtdHoras * valorHora     #letra a) #O salarioBrutoTotal seria o salario bruto sem o desconto do imposto de renda;
impostoRenda = salarioBrutoTotal * 0.11          #impostoRenda sera o valor que vai ser o valor do imposto que sera descontado do salarioBrutoTotal; 
salarioBruto = salarioBrutoTotal - impostoRenda  #O salarioBruto seria o salarioBrutol apos o desconto do imposto de renda;

pagouInss = salarioBruto * 0.08         #letra b) #calculo do desconto do INSS
pagouSindicato = salarioBruto * 0.05    #letra c) #calculo do desconto do Sindicato

#SalarioLiquido não inclui o impostoRenda pois ele ja esta descontado do salarioBruto, seria descontado 2x;     
salarioLiquido = salarioBruto - pagouInss - pagouSindicato   #letra d) #calculo do valor do salario liquido;
totalDescontos = salarioBruto - salarioLiquido               #letra e) #calculo do total de descontos em cima do salario bruto;

print('')                                                        #gambiarra para pular uma linha;
print('Salario bruto:         R$ {:.2f} '.format(salarioBruto))  #Imprime o valor do salario bruto;
print('Desconto do INSS:      R$ {:.2f}'.format(pagouInss))      #Imprime o valor do desconto do INSS;
print('Desconto do Sindicato: R$ {:.2f}'.format(pagouSindicato)) #Imprime o valor do desconto do Sindicato;
print('Salario liquido:       R$ {:.2f}'.format(salarioLiquido)) #Imprime o valor do salario liquido;
print('Total de descontos:    R$ {:.2f}'.format(totalDescontos)) #Imprime o valor total de descontos;

print('-------------------------------------------------------') #gambiarra para pular uma linha