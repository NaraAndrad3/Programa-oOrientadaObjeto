'''
Construa um algoritmo para o funcionamento de uma agenda. Devem ser lidos os seguintes 
dados de 10 pessoas: nome, endereço, CEP, bairro e telefone. Tais dados devem ser 
armazenados na agenda, cuja representação é uma lista com 10 linhas (referentes às 
pessoas) e 5 colunas (referentes aos dados). Por fim, o algoritmo deve gerar como saída a 
agenda impressa em ordem invertida em relação à ordem de entrada dos dados.
'''
#Tem que usar dicionários:
'''
10 pessoas
nome - endereço,cep,bairro e telefone
'''
agenda = list()
pessoa = dict()
max = 10
i=0
while i<max:
    pessoa.clear()
    pessoa['Nome'] = str(input('Digite o nome: '))
    pessoa['Endereço'] = str(input('Digite o endereço: '))
    pessoa['CEP']=int(input('Digite o cep: '))
    pessoa['Bairro']=str(input('Digite o bairro: '))
    pessoa['Telefone']=int(input('Digite o telefone: '))
    agenda.append(pessoa.copy())
    i+=1

agenda.reverse()

#print(agenda,'\n')
for i in agenda:
    print(i)

