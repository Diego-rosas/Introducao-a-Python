import time
from enviaEmail import enviaemail #importacao do modulo para enviar email, dentro já contem a biblioteca smtplib;

print('\nPara simular a entrada de temperatura do sensor.')
temp = int(input('Digite o valor uma temperatura: ')) #solicitacao de um valor de temperatura para simular a entrada
                                                     #atraves de um sensor;
tempLimite = 40             #variavel com o valor da temperatura limite segundo a questao

if temp > tempLimite:       #Condicional para comparar os valores de temperatura e verificar se precisa enviar a msg ou nao
    print('\nPara testar o recebimento do email.') 
    recebeEmail = input('Digite um email: ') #solicitacao de email para testar que esta enviando para qualqeur email
    #recebeEmail = 'DigiteSeuEmailAqui@gmail.com' #para testar sem precisar digitar um e-mail descomente a variavel 
    #e insira o seu e-mail e na hora de rodar o codigo so precisa apertar enter!
    hr = time.strftime('%H:%M')         #funcao para pegar o horario do alerta
    alerta = 'ALERTA DE TEMPERATURA!'    #mensagem de alerta
    corpo = ('{}º, {} - {}!'.format(temp, hr, alerta)) #variavel que vai receber o corpo das msgs
    enviaemail(corpo, recebeEmail)              #funcao para enviar o email, recebe como paramentero o corpo da msg,
                                                #e o email que vai receber o alerta
else:                                           #condicional para caso a temperatura seja menor que 40
    print('\nTEMPERATURA OK!\n')
