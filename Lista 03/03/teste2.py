import time
import os

a = ('  ___________')
b = (' /           |')
c = (' |           O')
d = (' |          /|\.')
e = (' |           |')
f = (' |          / \.')
g = (' |              ')
h = ('---             ')

forca = [a,b,c,d,e,f,g,h]
i = 0
tentativas = 6
while tentativas > 0:
    for i in range(9):
        for j in range(i):
            print(forca[j])
 #       time.sleep(.1)
        os.system('cls')
    tentativas -= 1
#os.system('cls')
#partesDoCorpo = {1:'Cabeça', 2:'Corpo', 3:'Braço Es', 4:'Braço Di', 5:'Perna Es', 6:'Perna Di'} # 6 tentativas ao todo