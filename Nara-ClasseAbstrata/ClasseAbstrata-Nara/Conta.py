import datetime
import abc
#Exercicios Herança Simples e Polimosfismo 
# Exercios Classe Abstrata
class Historico:
    def __init__(self):
        self.data_criacao = datetime.datetime.now()
        self.transacao = []

    def adicionar(self,t):
        self.transacao.append(t)

    def imprimir(self):
        print('conta criada em: {}'.format(self.data_criacao))
        for t in self.transacao:
            print('-',t)

class Cliente:
    def __init__(self,nome,sobrenome,cpf) :
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    def __repr__(self):
        return str(self.nome +'' +''+ self.sobrenome + '\nCPF: '+ self.cpf)

class Conta(abc.ABC):
    def __init__(self,nConta,cliente,saldo):
        self._nConta = nConta
        self._titular = cliente
        self._saldo = saldo
        self.historico = Historico()
    #set e get para o nConta
    @property
    def conta(self):
        return self._nConta
    
    @conta.setter
    def conta(self, cont):
        self._nConta = cont
        return self._nConta
    
    #set e get para titular
    @property
    def titularConta(self):
        return self._titular

    @titularConta.setter
    def titularConta(self, nome):
        self._titular = nome
        return self._titular
    #set e get para o saldo
    @property
    def saldoConta(self):
        return self._saldo
    
    @saldoConta.setter
    def saldoConta(self,valor):
        self._saldo = valor
        return self._saldo

    def listar(self):
        print('\nTitular: {}\nConta: {}\nSaldo: {}\n{}'.format(self._titular,self._nConta,self._saldo,self._tipo))

    def sacar(self, numero, valor):
        if numero == self._nConta:
            if valor > self._saldo:
                self.historico.adicionar('Saque não realizado')
            else:
                self._saldo -=valor
                self.historico.adicionar('Saque de {} realizado'.format(valor))
                
    def depositar(self,numero,valor):
        if numero == self._nConta:
            self._saldo +=valor
        self.historico.adicionar('Depósito realizado no valor de R$ {}'.format(valor))

    def transfere(self, origem,valor,destino):
        if origem == self._nConta:
            self.saldo-=valor
        if destino == self._nConta:
            self._saldo+=valor
            self.historico.adicionar('Transferencia de R$ {} realizada'.format(valor))
    def imprimirHistorico(self):
        self.historico.imprimir()

    @abc.abstractclassmethod
    def atualiza(self,taxa):
        #self._saldo += self._saldo*taxa
        pass
    
    #def __str__(self) -> str:
     #   return f'Conta: {self._nConta}\nTilular: {cliente}\nSaldo: {self._saldo}'
#Adicionando herança  
class ContaCorrente(Conta):
    def __init__(self,nConta,cliente,saldo,tipo) :
        super().__init__(nConta,cliente,saldo)
        self._tipo = tipo
    @property
    def tipo(self):
        return self._tipo
    def atualiza(self, taxa):
        self._saldo +=self._saldo*taxa*2

    def depositar(self, valor):
        self._saldo +=valor - 0.10
    def __str__(self) -> str:
        return f'Conta: {self._nConta}\nTilular: {cliente}\nSaldo: {self._saldo}\nTipo: {self.tipo}'

class ContaPoupanca(Conta):
    def __init__(self, nConta, cliente, saldo,tipo):
        super().__init__(nConta, cliente, saldo)
        self._tipo = tipo
    @property
    def tipo(self):
        return self._tipo
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
    def __str__(self) -> str:
        return f'Conta: {self._nConta}\nTilular: {cliente}\nSaldo: {self._saldo}\nTipo: {self.tipo}'

class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total
    @property
    def selic(self):
        return self._selic
    @selic.setter
    def selic(self,taxa):
        self._saldo_total = taxa
    
    def roda(self,conta):
        print('Saldo atual: {}'.format(conta._saldo))
        conta.atualiza(self._selic)
        self._saldo_total += conta._saldo
        print('Saldo Atualizado: ',conta._saldo)
        print('Saldo tota: ',self._saldo_total)
    @property
    def saldoTotal(self):
        return self._saldo_total
    @saldoTotal.setter
    def saldoTotal(self,valor):
        self._saldo_total = valor
class ContaInvestimento(Conta):
    def __init__(self, nConta, cliente, saldo,tipo):
        super().__init__(nConta, cliente, saldo)
        self._tipo = tipo
    @property
    def tipo(self):
        return self._tipo
    def atualiza(self,taxa):
       self._saldo += self._saldo * taxa *4
    def __str__(self) -> str:
        return f'Conta: {self._nConta}\nTilular: {cliente}\nSaldo: {self._saldo}\nTipo: {self.tipo}'

#Testes
#Esse main são os testes pedidos nas atividades de herança, classe abstrata e polimorfismo
if __name__ == '__main__':
    cliente = Cliente('Nara','Dias','1234-5')
    #conta = Conta(123,cliente,1000)  Essa classe não pode ser instanciada pq é abstrata
    #Adicionei mais um atributo pq implementei os tipos de conta no outro codS
    contaC = ContaCorrente(135,cliente,1000,'Conta Corrente')
    contaP = ContaPoupanca(145,cliente,1000,'Conta Poupança')
    contaInvest = ContaInvestimento(890,cliente,1000,'Conta Investimento')
    #conta.atualiza(0.1)
    contaC.atualiza(0.1)
    contaP.atualiza(0.1)
    contaInvest.atualiza(0.1)

   # print('Conta: ',conta._saldo)
    print('Conta Cor: ',contaC._saldo)
    print('Conta Pou: ',contaP._saldo)
    print('Conta ivest: ',contaInvest._saldo)
    #testando a saida amigável
    #print(conta,'\n')
    print(contaC,'\n')
    print(contaP,'\n')
    print(contaInvest,'\n')

    at = AtualizadorDeContas(0.1)
    at.roda(contaP)
    at.roda(contaC)
    at.roda(contaInvest)
   # at.roda(conta)
