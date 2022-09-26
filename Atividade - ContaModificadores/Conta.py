import datetime
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
class Conta:
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
        print('\nTitular: {}\nConta: {}\nSaldo: {}\n'.format(self._titular,self._nConta,self._saldo))

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
