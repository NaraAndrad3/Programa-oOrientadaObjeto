def fatorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fatorial(n -1)

n = int(input('Digite um número:\n'))
#fatorial(n)
y = fatorial(n)
print('fatorial ', y)