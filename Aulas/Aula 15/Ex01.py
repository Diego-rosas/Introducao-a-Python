#Execicio 01 da aula 15 sobre POO

class Televisao():
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = None
        self.marca = None 


tv1 = Televisao()
tv1.tamanho = '55"'
tv1.marca = 'LG'
print('tv1:')
print(tv1.ligada) 
print(tv1.canal)
print(tv1.tamanho)
print(tv1.marca) 
print('-------------------------')
tv2 = Televisao()
tv2.tamanho = '32"'
tv2.marca = 'Samsung'
print('tv2:')
print(tv2.ligada, tv2.canal, tv2.tamanho, tv2.marca)
