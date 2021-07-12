from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#cria o objeto da menssagem 
msg = MIMEMultipart()

message = 'pegou email novo'

#define os parametros da menssagem 
password = '#enviaEmail7'
msg['From'] = 'enviae7@gmail.com'
msg['To'] = 'diego.rosas@ufpe.br'
msg['subject'] = 'email de teste'

#adiciona ao corpo da msg
msg.attach(MIMEText(message, 'plain'))

#cria servidor
server = smtplib.SMTP('smtp.gmail.com: 587') #host,port
server.starttls()

#credenciais de login para enviar o email
server.login(msg['From'], password)

#envia a menssagem via servidor 
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print('Email enviado com sucesso para : %s' % (msg['To']))