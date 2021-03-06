import time
import random
from enviaEmail import enviaemail #importacao do modulo para enviar email, dentro já contem a biblioteca smtplib;

temp = random.randint(1,100)             #sorteia um valor de 0 a 100 para simular a entrada de um valor lida por um sensor 
                                            #de temperatura 
print('\nTemperatura atual = {}º'.format(temp)) #imprime o valor sorteado como se fosse a temperatura lida               

tempLimite = 40             #variavel com o valor da temperatura limite segundo a questao

if temp > tempLimite:       #Condicional para comparar os valores de temperatura e verificar se precisa enviar a msg ou nao
    #Para testar o recebimento do email.
    recebeEmail = 'diegorosas19@gmail.com' #para testar o recebimento do e-mail, insira o seu e-mail nesta variavel                                          
    hr = time.strftime('%H:%M')         #funcao para pegar o horario do alerta
    alerta = 'ALERTA DE TEMPERATURA!'    #mensagem de alerta
    corpo = ('{}º, {} - {}!'.format(temp, hr, alerta)) #variavel que vai receber o corpo das msgs
    enviaemail(corpo, recebeEmail)              #funcao para enviar o email, recebe como paramentero o corpo da msg,
                                                #e o email que vai receber o alerta
else:                                           #condicional para caso a temperatura seja menor que 40
    print('\nTEMPERATURA OK!\n')                #imprime um aviso que a temperatura esta ok 
