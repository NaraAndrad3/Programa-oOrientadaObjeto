import random
def Gabarito():
    gabarito = []
    for i in range(0,13):
        gabarito.append(random.randint(1,3))
    return gabarito

def Apostador():
    jogador=[]
    for i in range(0,13):
        jogador.append(random.randint(1,3))
    return jogador
def processo(gabarito, jogador):
    max = 13
    acertos = 0
    for i in range(0,max):
        if gabarito[i] == jogador[i]:
            acertos+=1
    return acertos

#Código principal
gabarito = Gabarito()
print(gabarito)
max = 13
cartao = []
acertos = 0
n_jog=0
print('O gabarito do jogo é: {}'.format(gabarito))
while n_jog<3:
    jogador = Apostador()
    acertos = processo(gabarito,jogador)
    n_jog+=1
    print('O jogador n° {} , fez a jogada {} marcou {} acertos!!'.format(n_jog,jogador,acertos))
    if acertos == max:
        print('GANHADOR!!!')
    
    

