''''
Crie uma classe para representar uma pessoa, com os atributos privados de nome, data de nascimento e altura. 
Crie os métodos públicos necessários para sets e gets e também um método para imprimir todos os dados de 
uma pessoa. Crie um método para calcular a idade da pessoa.
'''
import datetime
registro={}
class Pessoa:
    def __init__(self,nome,dia,mes,ano,altura):
        self._nome = nome
        self._dia = dia
        self._mes = mes
        self._ano = ano
        self._altura = altura
    #Set e Get do nome da pessoa
    @property
    def nomePessoa(self):
        return self._nome
    @nomePessoa.setter
    def nomePessoa(self,name):
        self._nome = name
    #Set e Get do dia da nescimento
    @property
    def diaNasc(self):
        return self._dia
    @diaNasc.setter
    def diaNasc(self,day):
        self._dia = day
    #Set e Get do mes de nascimento
    @property
    def mesNasc(self):
        return self._mes
    @mesNasc.setter
    def mesNasc(self,month):
        self._mes = month
    #Set e Get do ano de nascimento
    @property
    def anoNasc(self):
        return self._ano
    @anoNasc.setter
    def anoNasc(self,year):
        self._ano = year
    #Set e Get da altura
    @property
    def alturaPessoa(self):
        return self._altura
    @alturaPessoa.setter
    def alturaPessoa(self,height):
        self._altura = height

    def __str__(self) :
        return str(f'Dados: \nNome: {self._nome} Dia: {self._dia} Mes: {self._mes} Ano: {self._ano} Altura: {self._altura}' )

def calcIdade(dia,mes,ano):
        dataAtual = datetime.date.today()
        data = datetime.date(ano,mes,dia)
        idade = dataAtual.year - data.year
        if dataAtual.month < data.month:
            idade-=1

        return idade

def imprimir():
        for i in registro.values():
            print(i)

esc = int(input('1-Adicionar Pessoa\n2-Sair\nSelecione: '))
while esc != 2:
    if esc ==2:
        break
    if esc == 1:
        nome = str(input('Nome: '))
        dia = int(input('Dia de nascimento: '))
        mes = int(input('Mes de nascimento: '))
        ano = int(input('Ano de Nascimento: '))
        altura = float(input('Altura: '))
        idade = calcIdade(dia,mes,ano)
        print('A idade da pessoa é: ',idade)
        pessoa = Pessoa(nome,dia,mes,ano,altura)
        registro[nome] = pessoa
        imprimir()
    esc = int(input('1-Adicionar Pessoa\n2-Sair\nSelecione: '))



