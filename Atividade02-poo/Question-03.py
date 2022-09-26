palavra = str(input('Digite: '))
caractere = str(input('Digite o caractere a ser buscado na string: '))
pos = 0
i=0
lis_pos=[]
lista=[]
tam = len(palavra)
while tam > i:
    if caractere == palavra[i]:
        pos= i 
        lis_pos.append(pos)
    i+=1   
print('O caractere encontrado foi: {} na posição: {}'.format(caractere,lis_pos ))