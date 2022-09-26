import operator
placar ={}
n=2
for i in range(1,n+1):
    nome = str(input('Nome do corredor: '))
    volta1 = float(input('Tempo da volta 1: '))
    volta2 = float(input('Tempo da volta 2: '))
    volta3 = float(input('Tempo da volta 3: '))
    placar[nome] = [volta1,volta2,volta3]

print(placar)

volta = 0
media = dict()
soma = 0
melhor_volta = placar[nome][0]
for chave in placar:
    for i in placar[chave]:
        if i < melhor_volta:
            melhor_volta = i
            nome = chave
        soma += i
    media[chave] = soma / 3
ordem = sorted(media.items(), key=operator.itemgetter(1))
for i in range(0, n):
    print("{}° lugar: {} - {} segs.".format(i+1,ordem[i][0], ordem[i][1] ))

print(melhor_volta)



