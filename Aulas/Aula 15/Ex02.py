#Execicio 01 da aula 15 sobre POO

class Televisao():
    
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = None
        self.marca = None 
        self.muda_canal = None
    

tv3 = Televisao()
print(tv3.canal)
print(tv3.muda_canal)