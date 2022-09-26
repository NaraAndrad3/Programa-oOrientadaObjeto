'''
alunos={
'nome':[nota1,nota2], ...
}
'''
#Dicionário
alunos = {}
quant = int(input('Quantos alunos quer inserir: '))
i=0
media = 0
while i<quant:
    nome=str(input('Digite o nome: '))
    nota1=float(input('Digite a nota 1: '))
    nota2=float(input('Digite a nota 2: '))
    #estou atribuindo os valores à chave nome
    alunos[nome] = [nota1, nota2]
    i+=1
esc = 1
name = str(input('Digite o nome do aluno: '))
if name not in alunos:
    print('O aluno digitado não consta no registro:')
    name = str(input('Digite um nome válido: '))

aluno = alunos[name]
media = (aluno[0]+aluno[1])/2
print(45*'-')
#print(alunos)
print('A média do aluno {} é {}'.format(name,media))