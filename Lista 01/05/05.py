#Questao 05
#por: Diego Rosas

print('-------------------------------------------------------') #gambiarra para pular uma linha
print('                  CALCULADORA DE AUMENTOS              ') #titulo de enfeite
print('-------------------------------------------------------') #gambiarra para pular uma linha

salario = int(input('Qual o valor do salario[R$]? ')) #Variavel que vai receber o valor do salario 
pctg = int(input('Qual a porcentagem de aumento? '))  #Variavel que vai receber a taxa da porcentagem de aumento  

pctgValor = (salario * pctg) / 100                    #Calculo do valor da porcentagem de aumento relacionada ao valor do salario

salarioNovo = salario + pctgValor                     #Calculo do novo salario depois que eh aplicada a taxa de aumento
print('')                                                           #gambiarra para pular uma linha
print('Voce recebera um aumento de: R$ {:.2f}'.format(pctgValor))   #Imprime o valor do aumento
print('Seu novo salario sera: R$ {:.2f}'.format(salarioNovo))       #Imprime o valor do novo salario

print('-------------------------------------------------------')    #gambiarra para pular uma linha