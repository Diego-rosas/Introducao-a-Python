x = ['teste1','teste2','teste3','teste1','teste1','teste1','teste1']
qt = []
for i in range(len(x)):
    y = x[i]
    qt.append( x.count(y))
    #print (y)
print (qt)    

dic = dict(zip(x,qt))
print(dic)