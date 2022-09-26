dicio = {
    'nara':[1,2,3,4,5],
    'Raquel':[10,9,8,7]
}
media =[]
m=0
for chave, lista1 in dicio.items():
    print(chave)
    for i in lista1:
        print(i)
        m = m+i
    media.append(m)
    m=0
print(dicio['Raquel'][0])
print('A media é: {}'.format(media))
nom=''
menor=dicio['nara'][0]
for chave, lista1 in dicio.items():
    for i in lista1:
        if i<menor:
            menor = i
    nom = chave    
            
        
            
            
print(nom)
print('O menor tempo é: {}'.format(menor))