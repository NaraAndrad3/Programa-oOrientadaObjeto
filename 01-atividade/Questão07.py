def binar(num):
    resto = 0
    if num == 0:
        return '0'
    else:
        binario = ''
        while num>1:
            resto = num%2
            num = int(num/2)
            binario +=str(resto)
        binario+='1'
    return binario[-1::-1]


num = int(input('Digite um número:\n'))
x = binar(num)
print('O número em binário é:' + x)






