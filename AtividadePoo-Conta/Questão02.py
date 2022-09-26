'''. Crie uma classe Agenda que pode armazenar 10 pessoas (Classe com os atributos: nome, idade, altura) e que 
seja capaz de realizar as seguintes operações: 
a. armazenaPessoa; // Não permitir armazenar mais de 10 pessoas'''
agenda = {}
class Agenda:
    def __init__(self,nome,idade,altura):
        self._nome = nome
        self._idade = idade
        self._altura = altura
    #set e get do nome
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,name):
        self._nome = name
    
    #set e get da idade
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self,age):
        self._idade = age
    
    #Set e Get da altura
    @property
    def altura(self):
        return self._altura 
    @altura.setter
    def altura(self,alt):
        self._altura = alt

    def __str__(self) -> str:
        return str(f'Nome: {self._nome}\nIdade: {self._idade}\nAltura: {self._altura}')

def removePessoa():
    nome = str(input('Digite o nome a ser removido: '))
    if nome in agenda:
        del agenda[nome]
    else:
        print('Registro não encontrado.')
        
def buscarPessoa():
    nome = str(input('Digite o nome: '))
    if nome in agenda:
        print(agenda[nome])
    else:
        print('Registro não encontrado.')

def imprimirAgenda():
    for  i in agenda.values():
        print('\n',i,'\n')

print('1-Adicionar pessoa\n2- Remover pessoa\n3-Buscar\n4-Imprimir agenda\n5-Sair')
esc = int(input('Selecione: '))
while esc !=5:
    if len(agenda) == 3:
        print('Limite atingido.')
        break
    if esc ==1:
        # Adicionar pessoa
        nome = str(input('Nome: '))
        if nome in agenda:
            print('Digite o nome e sobrenome: ')
            nome = str(input('Nome e sobrenome: '))

        idade = int(input('Idade: '))
        altura = float(input('Altura: '))
        pessoa = Agenda(nome,idade,altura)
        agenda[nome] = pessoa
    if esc ==2:
        removePessoa()
    if esc ==3:
        buscarPessoa()
    if esc ==4:
        imprimirAgenda()

    esc = int(input('Digite uma nova opção: '))
    