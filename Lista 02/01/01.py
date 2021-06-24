#Questao 01
#Por: Diego Roberto
#Progrma para calcular se um emprestimo vai sera provado ou nao
print('')                                                    #pula uma linha
print('----------CALCULADORA DE EMPRESTIMOS ----------')     #titulo ficticio
valorCasa = float(input('Qual o valor da casa? R$ '))        #variavel que recebe o valor da casa
salario = float(input('Qual o seu salario mensal? R$ '))     #variavel que recebe o valor do salario
qtdAnos = int(input('Em quantos anos pretende pagar? '))     #variavel que recebe a quantidade de ano que o emprestimo vai ser pago
print('')                                                    #pula uma linha

pctSalario = salario * 0.3                       #Calculo da porcentagem de 30% do salario

prestacao = valorCasa / (qtdAnos *12)            #Calculo para saber o valor da prestacoes mensal que tera que ser paga

if prestacao > pctSalario:                       #Compara o valor da prestacao com a procentagem do salario
    print('Emprestimo não aprovado!')            #Se o valor da prstacao for maior, o emprestimo nao sera aprovado. Vai imprimir essa mesnagem;
else:
    print('Emprestimo aprovado!')              #Se a porcentagem do salrio for maior, o emprestimo vai ser aprovado. Vai imprimir essa mensagem;          

print('')                                       #pula uma linha