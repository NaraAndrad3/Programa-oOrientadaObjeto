''''
Gere uma lista de 100 números inteiros de 1 até 100. Apenas usando as funções básicas
(não use bibliotecas científicas tais como numpy, panda ou scipy). Calcule
'''
from random import randint
import functools as ft
def media(numeros):
    media = 0
    soma=0
    tam = len(numeros)
    for i in numeros:
        soma = soma+i
    media = soma/tam
    return media
#O :.2f é para formatar o float a 2 casas decimais
def varianca(n):
    m = media(numeros)
    return float('{:.2f}'.format((n-m)**2))#aqui estou convertendo esse valor para float

def desvio(n,m):
    return n+m

def mediana(numeros):
    mediana = 0
    numeros.sort()
    print('Os números ordenados: {}'.format(numeros))
    tam = len(numeros)
    if tam%2==0:
        m1 = numeros[tam//2]
        m2=numeros[tam//2-1]
        mediana = (m1+m2)/2
        print('A mediana é: {}'.format(mediana))
    else:
        mediana = numeros[tam//2]
        print('A mediana é: {}'.format(mediana))

#Código principal:
numeros = []
for i in range(0,12):
    numeros.append(randint(1,10))
print(numeros)
med=media(numeros)
print('A média é: {}'.format(med))
aux=[]
tam = len(numeros)
x=0
#A variança é i-media ao quadrdo
#O map para aplicar a função variança em cada elemento da lista numeros
aux=list(map(varianca,numeros))
#Reduce para somar todos os elementos da lista aux
desv = ft.reduce(desvio,aux)
mediana(numeros)
print('A variança é:{}'.format(aux))
print('O desvio padrão é: {:.2f}'.format(desv))




