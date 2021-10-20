import random

def sortear():
    sorteado = random.randint(1,100)
    return sorteado

def inputNumber():
    vencedor = sortear()
    count = 1
    while(True):
        numero = int(input('Digite o numero sorteado: '))
        count+=1
        if(vencedor==numero):
            print('Com ', count,' tentativas, ','Você acertou! o numero é: ', vencedor)
            break
        elif(numero<vencedor):
            print('Passou perto!')
        elif(numero>vencedor):
            print('Passou longe!')
        else:
            continue