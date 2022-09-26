nome = 'abacate'
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
alfabeto =list(alfabeto)
nome = list(nome)
nome.sort()
print(alfabeto)
other =[]
for i in alfabeto:
    if i in nome:
        n =nome.count(i)
        for y in range(0,n):
            other.append(i)

print(other)