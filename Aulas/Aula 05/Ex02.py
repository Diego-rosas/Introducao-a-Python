#
idadeMoto = int(input("Qual o ano da sua moto? "))

#modo 1 de fazer
'''if idadeMoto > 3:
    print("Sua moto é antiga. Bora trocar!")
else:
    print("Sua moto ainda é nova!")'''

#modo 2 de fazer
'''if idadeMoto <= 3:
    print("Sua moto ainda é nova!")
else:
    print("Sua moto é antiga. Bora trocar!")'''

#modo 3 de fazer
if idadeMoto <= 3:
    print("Sua moto tem {} anos, ela ainda é nova!".format(idadeMoto))
else:
    print("Sua moto tem {} anos, ela é antiga. Bora trocar!".format(idadeMoto))
