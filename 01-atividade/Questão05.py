def fatorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fatorial(n -1)       
def arranjo(num1, n):
    arran =0
    arran = (fatorial(n)/fatorial(n-num1) )
    print('O arranjo é: {}'.format(arran))

def combinacao(num1, n):
    comb = 0
    comb = (fatorial(n)/(fatorial(num1) * fatorial(n-num1)))
    print('A combinação é: {}'.format(comb))

n = int(input('Digite um número:\n'))
y = fatorial(n)
print('fatorial ', y)
num1= int(input('Digite um número'))
arranjo(num1, n)
combinacao(num1, n)



