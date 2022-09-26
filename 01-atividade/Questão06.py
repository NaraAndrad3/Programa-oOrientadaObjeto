def primo(num):
    cont = num%2
    if cont ==0:
        return False
    elif cont == 1:
        print(num)
    else:
        print('Não existe primo neste intervalo')

n = int(input('Digite um número:\n'))
n2= int(input('Digite um número:\n'))

for i in range(n,n2):
     primo(i)
   




