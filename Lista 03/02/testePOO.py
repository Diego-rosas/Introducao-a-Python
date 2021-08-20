class Figuras:
    def __init__(self,b,h):
        self.base = b
        self.altura = h
        self.area = (b*h)/2
    def mostrar(self):
        print('A area eh igual a: {} m²'.format((self.base*self.altura)/2))
        print('A area eh igual a: {} m²'.format(self.area))


b = float(input('Digite o valor da base: '))
h = float(input('Digite o valor da altura: '))

triangulo = Figuras(b,h)
triangulo.mostrar()