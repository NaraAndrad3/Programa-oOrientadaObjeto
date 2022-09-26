import random
n_tentativas = 10
i=1

secret = random.randint(0,100)
#print('O número secreto é: {}'.format(secret))
while i<n_tentativas:
    num=int(input('Digite o número secreto:'))
    print('Tentativa número:{}'.format(i))
    if num==secret:
        print('Você acertou o número!')
        esc = int(input(('Deseja Reiniciar?\n1-Sim\n2-Não')))
        if esc == 1:
            i=1
            secret = random.randint(0,100)
            #print('O novo número é: {}'.format(secret))
            num=int(input('tentativa número: {}\nDigite o número secreto:'.format(i)))
        else:
            break
    i+=1
    if i == n_tentativas:
        print('Você Perdeu!!!!')
        break

        

