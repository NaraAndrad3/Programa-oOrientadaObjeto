import abc
class Funcionário(abc.ABC):#funcionários comuns
    def __init__(self,nome,cpf,salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    @abc.abstractclassmethod
    def bonificacao(self):
        pass

#essa classe vai herdar todos os stributos da classe Funcionário
class Gerente(Funcionário):
    def __init__(self,nome,cpf,salario,senha,gerenciados):
        super().__init__(nome,cpf,salario)#está referenciando a classe mãe(Funcionário)
        self.senha = senha
        self.gerenciados = gerenciados
    @property
    def bonificacao(self):
        return self.salario*0.15

class Secretaria(Funcionário):
    def __init__(self, nome, cpf, salario,qtd_chaves):
        super().__init__(nome, cpf, salario)
        self.qtd_chaves = qtd_chaves
    @property
    def bonificacao(self):
        return self.salario * 0.1+30
    


gerente = Gerente('Raquel','9876-4',5000,1010,3)
secretaria = Secretaria('Dias','09876-2',1550,3)
print(gerente.bonificacao)
print(secretaria.bonificacao)
print(vars(gerente))