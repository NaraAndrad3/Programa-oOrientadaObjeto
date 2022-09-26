def fatorial(n):
    fat = 1 
    i = 1
    if n == 1 or n==0:
        print(1)
    else:
        
        while n >=i:
            fat = fat*i
            i +=1      
    print('Fatoria iterativo :{}'.format(fat))


    
n = int(input('Digite um numero \n'))
fatorial(n)