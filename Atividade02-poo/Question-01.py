def tamString(palavra):
    cont =0
    for i in palavra:
        cont +=1
    return cont
    
palavra = str(input('Digite uma palavra: '))
cont = tamString(palavra)
print('O tamanho da string é: {}'.format(cont))

