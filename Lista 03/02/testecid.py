def multiplicaV():
        total = 1
        print('Digite os numeros que deseja mutiplicar e 1 para sair: ')
        while True:
            num = float(input('* '))
            total = total * num
            if num == 1:
                break
        if total%2 == 0 or total%2 == 1:
            print('Total = {} '.format(int(total)))
        else:
                print('Total = {} '.format(total))

#multiplica()

def sub():
    fator=[]        #vai receber o array de numeros
    while True:     # coleta dados para a subtração
        number = input('digite os valores a subtrair: ')        #requisitando os termos
        while number != "=" and number.isnumeric()!= True:      # se não achar sinal de = ou um numero pede de novo
          number = input('você precisa digitar um numero ou sinal = para continuar:')       #pedindo de novo 
        if number.isnumeric():          #se for numerico add ao vetor
            fator.append(float(number))         #add ao vetor
        elif number=='=':       # se for igual sai do while e vai para ao passo de subtrair
            if len(fator) >= 2: # se mandar = sem ter numeros sufcientes continua pedindo
                break               #saindo da captura de dados
    
    i=1# incremento do prox while -> começa da seguda posição do vetor
    result= fator[0] #porquê a primeira já está sendo passada aqui 
    while True:
        if i==(len(fator)): #i não pode ser igual a ultima posição
            break          #porquê vai sair do len do vetor
      
        result = result - fator[i]  #vetor [1][2][3] result seria = 1 e fator[i] = 2 em seguida result seria
        i=i+1                       #o resultadoda primeira operação e fator[i] seria o prox term da prox operação
    
    return(result)

print(sub())