media1 = float(input('Digite a media da disciplina 1:'))
media2 = float(input('Digite a media da disciplina 2:'))
media3 = float(input('Digite a media da disciplina 3:'))
media4 = float(input('Digite a media da disciplina 4:'))

mediaDasDisciplinas = media1>=media2 and media2>=media3 and media3>=media4 #Forma de verificar se todas medias são maores ou iguais a media que é 7
#se uma deleas for menor que as outras vai dar falso
print ('{}'.format(mediaDasDisciplinas))