lista=[1,2,7,4,5,6,10,5,9,3]
lista2=[1,7,3,4,5,6,7,8,9,10]
resultado = []
val=0
for i in range(0,10):
    for y in range(0,10):
        if i==y:
            val = lista[i]*lista2[i]
            resultado.append(val)
print('A lista com os resultados é: {}'.format(resultado))
