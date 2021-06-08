stg1 = input("Digite a string 1: ") #variavel que receberá a string 1
stg2 = input("Digite a string 2: ") #variavel que receberá a string 2

tamanhoStg1 = len(stg1) #Variavel que vai gravar o tamanho da string 1
tamanhoStg2 = len(stg2) #Variavel que vai gravar o tamanho da string 2

print("O conteudo da string 1 é: ", stg1) #Imprime o conteúdo da string 1
print("O conteudo da string 2 é: ", stg2) #Imprime o conteúdo da string 2
print("O tamando da string 1 é: ", tamanhoStg1) #Imoprime o tamanho da string 1
print("O tamando da string 2 é: ", tamanhoStg2) #Imoprime o tamanho da string 2

if stg1 == stg2:                                  #Estrura condicional que vai verificar se as strings são iguais.
    print("As strings tem o mesmo tamanho e o mesmo conteudo!") 
elif tamanhoStg1 == tamanhoStg2 and stg1 != stg2:  #Estrura condicional que vai verificar se as strings tem tamanho iguais e conteudo diferente.
    print("As strings tem o mesmo tamanho, porem contudo diferente!")
else:                                        #Estrura condicional para caso as strings sejam totalmente diferentes.
    print("As estrings não são iguais!")

 


        

        