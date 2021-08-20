import  smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText

#funcao para enviar o email, recebe como paramentero o corpo da msg, e o email que vai receber o alerta;
def enviaemail(corpo, recebeEmail):
    #1 - Startar o servidor SMTP
    host = 'smtp.gmail.com'
    port = '587'
    login = 'enviae7@gmail.com'
<<<<<<< Updated upstream
    senha = '#enviaEmail7' 
=======

    with open('01\senha.txt', 'r', encoding='utf-8') as arquivo:
        senha = arquivo.read() 
>>>>>>> Stashed changes
  
    server = smtplib.SMTP(host,port)
    server.ehlo()
    server.starttls()
    #credenciais de login para enviar o email
    server.login(login,senha)

    #2- CONSTRUIR O EMAIL TIPO MIME
    #corpo = '' - enivado via parametro
    #Montando o e-amil
    email_msg = MIMEMultipart()
    email_msg['From'] = 'enviae7@gmail.com'
    email_msg['To'] = recebeEmail # 'diego.rosas@ufpe.br' - enviado via parametro
    email_msg['subject'] = 'ALERTA!!'
    email_msg.attach(MIMEText(corpo, 'plain')) #adiciona ao corpo da msg

    #3 - ENVIAR O EMAIL TIPO MIME NO SERVIDOR SMTP
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    server.quit()
    #Mensagem de aviso
    print('\nAlerta enviado com sucesso!\n')
