#Questao 06
#Por: Diego Rosas
#data: 21/07/2021

from lorem_text import lorem

paragrafos = lorem.paragraphs(5)

arquivo = open('06\\arquivo.txt','a+')
conteudo = arquivo.write(paragrafos)

arquivo = open('06\\arquivo.txt')
conteudo = arquivo.read()

print('\n',conteudo)

arquivo.close()

