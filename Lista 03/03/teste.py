import os
p = 'teste'
t = []
print(len(p))

print('  '.join(p))
for i in range(len(p)):
    c = ('- ')
    t.append(c)
    print('{}'.format(c), end=' ')


#print(' '.join(c))
print('\n',len(t))

tentativas = []
while True:
    l = input('digite uma letra: ')
    if l in p:
        indiceL = p.find(l)
        p = p.replace(l, '')
        #print(indiceL)
        tentativas.append(l)
        print(''.join(tentativas))
        print(p)
        #print(new_pl)
    if len(p) == 0:
        break
#    os.system('cls')