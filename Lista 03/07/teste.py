#Questao 07
#Por: Diego Rosas
#data: 21/07/2021
#Programa que para criar uma agenda telefonica

#abre o arquivo 
agenda = open('07\\agenda.docx','w')
agenda = open('07\\agenda.docx','a+')
contatos = agenda.write('teste2')
agenda = open('07\\agenda.docx')
x = agenda.read()
#print(contatos)
print(x)
agenda.close()

