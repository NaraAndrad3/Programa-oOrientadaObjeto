import datetime
import random
import abc
import datetime
import math
registro = {}
cPoupanca = {}
cCorrente = {}
segVida = {}
lista2 = []
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
    
   
class Pessoa(abc.ABC):
    def __init__(self,nome, cpf, nascimento):
        self._nome = nome
        self._cpf = cpf
        self._nascimento = nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,name):
        self._nome = name

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self,reg):
        self._cpf = reg

    @property
    def dataNascimento(self):
        return self._nascimento

    @dataNascimento.setter
    def dataNascimento(self,data):
        self._nascimento = data
    @abc.abstractmethod
    def verificar(self,n):
        while True:
            if self._titular.cpf == n:
                return 1
            else:
                return 0

#Cadastrar funcionário (Atributos: nome, cpf, data de nascimento, salário)
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, nascimento,salario,tipo):
        super().__init__(nome, cpf, nascimento)
        self._salario = salario
        self._tipo = tipo
    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self,valor):
        self._salario = valor
    @property
    def tipo(self):
        return self._tipo

    def verificar(self,n):
        while True:
            if self._titular.cpf == n:
                return 1
            else:
                return 0

    def __repr__(self) -> str:
        return f'\nNome: {self._nome}\nCPF: {self._cpf}\nNascimento: {self._nascimento}\nTipo: {self._tipo}\n'   
#Cadastrar cliente (Atributos: nome, cpf, data de nascimento, profissão)
class Cliente(Pessoa):
    def __init__(self, nome, cpf, nascimento,profissao,tipo):
        super().__init__(nome, cpf, nascimento)
        self._profissao = profissao
        self._tipo = tipo
    @property
    def profissao(self):
        return self._profissao
    @profissao.setter
    def profissao(self,pr):
        self._profissao = pr
    @property
    def tipo(self):
        return self._tipo
    def verificar(self,n):
        while True:
            if self._titular.cpf == n:
                return 1
            else:
                return 0

    def __str__(self) -> str:
        return f'\nNome: {self._nome}\nCPF: {self._cpf}\nNascimento: {self._nascimento}\nProfissão: {self._profissao}\nTipo: {self._tipo}'
    

#Criar conta corrente (Atributos: número, saldo, histórico de transações)
class Conta(abc.ABC):
    _totalConta = 0
    def __init__(self, nConta,saldo,tipo,total):
        self._nConta = nConta
        self._saldo = saldo
        self._tipo = tipo
        self._total = total
        type(self)._totalConta+=1
        self.historico = Historico()

    @classmethod
    def totalcontas(cls):
        return cls._totalConta
    
    @property
    def total(self):
        return self._total
    @total.setter
    def total(self,v):
        self._total +=v

    @property
    def nconta(self):
        return self._nConta
    @nconta.setter
    def nconta(self,n):
        self._nConta = n
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self,sald):
        self._saldo = sald
    @property
    def tipo(self):
        return self._tipo
    
    def sacar(self,numero,valor):
        if numero == self._nConta:
            if self._saldo < valor:
                print('Conta não encontrada')
                self.historico.adicionar('Saque não realizado')       
        else:
             self._saldo -= valor
             self.historico.adicionar('Saque realizado. Valor: {}'.format(valor))
            
    def depositar(self,numero,valor):
        if numero == self._nConta:
            self._saldo += valor
            print('Deposito realizado com sucesso!')
            self.historico.adicionar('Deposito realizado no valor: {}'.format(valor))
        elif numero not in cCorrente:
            print('Conta não encontrada!')
            self.historico.adicionar('deposito não realizado') 


    def transferir(self,origem, valor, destino):
        if origem == self._nConta:
            self._saldo -=valor
            if destino == self._nConta:
                self._saldo +=valor
                self.historico.adicionar('Trasferencia realizada. Valor: {}'.format(valor))
            else:
                print('Conta não encontrada')
        else:
            print('Conta não encontrada')

    def imprimirHistorico(self):
        self.historico.imprimir()
    
    @abc.abstractmethod
    def tributacao(self,tributos):
        self._total += 10 + (self.saldo * tributos)

    def __repr__(self) -> str:
        return str(self._nConta + self._saldo)
    

class ContaCorrente(Conta):
    def __init__(self, nConta,cliente, saldo, tipo, total):
       super().__init__(nConta, saldo, tipo, total)
       self._titular = cliente


    def __str__(self) -> str:
        return f'\nConta: {self._nConta}\nTiTular: {self._titular}\nSaldo: {self._saldo}\nTipo da Conta: {self._tipo}\n'

    def verificar(self,n):
        while True:
            if self._titular.cpf == n:
                return 1
            else:
                return 0
    
    def listar(self):
        print(f'\nTitular: {self._titular}\nN° Conta: {self._nConta}\nSaldo: {self._saldo}\nTipo da conta: {self._tipo}\n')

    def tributacao(self,tributos):        
        lista = []
        self._total = 10 + self.saldo * tributos
        lista.append(self.total)
        return lista
        
           
class ContaPoupanca(Conta):
    def __init__(self, nConta, saldo,cliente, tipo,total):
        super().__init__(nConta, saldo, tipo,total)
        self._titular = cliente
    def __str__(self) -> str:
        return f'\nConta: {self._nConta}\nTiTular: {self._titular}\nSaldo: {self._saldo}\nTipo da Conta: {self._tipo}\n'

    def verificar(self,n):
        while True:
            if self._titular.cpf == n:
                return 1
            else:
                return 0
                
    def tributacao(self,tributos):
        self._total = 10 + (self.saldo * tributos)

    def listar(self):
        print(f'\nTitular: {self._titular}\nN° Conta: {self._nConta}\nSaldo: {self._saldo}\nTipo da conta: {self._tipo}\n')
    
            
class Tributacao:
    _contador = 0
    def __init__(self,totalTributos,historico = Historico()):
        self._totalTributos = totalTributos
        self._historico = historico
        type(self)._contador +=1

    def tributa(self,conta):
        soma=0
        for i in cCorrente.values(): 
            tributos = 0.01
            soma += sum(conta.tributacao(tributos))
        print(soma)
                      
    @property
    def totalTributos(self):
        return self._totalTributos

#valor mensal, valor total do seguro
class SeguroDeVida:
    def __init__(self,cliente2,valorMensal,valorTotal,total):
        self._titular = cliente2
        self._valorMensal = valorMensal
        self._valorTotal =  valorTotal   
        self._total = total
    @property
    def total(self):
        return self._total
    @total.setter
    def total(self,v):
        self.total +=v  
    @property   
    def valorMensal(self):
        return self._valorMensal
    @valorMensal.setter
    def valorMensal(self,v):
        self._valorMensal = v
    
    @property
    def valorTotal(self):
        return self._valorTotal
    @valorTotal.setter
    def valorTotal(self,vt):
        self._valorTotal = vt
    
    def calcTributo(self):
        self._total = self._valorMensal * 0.02
        return self._total

    def __repr__(self) :
        return f'Titular: {self._titular}\nValor Mensal: {self._valorMensal}\nValor Total: {self._valorTotal}'
    
    def listar(self):
        print(f'Titular: {self._titular}\nValor Mensal: {self._valorMensal}\nValor Total: {self._valorTotal}')

def cadastrar_ContaCorrente():
    cont = 0
    print('\tCadastrar Conta Corrente:')
    cpf = str(input('CPF: '))
    for i in cCorrente.values():
        cont = i.verificar(cpf)
        if cont == 0:
            print('Não é possivel criar uma conta desse tipo')
        else:
            nome = str(input('Nome: '))
            #cpf = str(input('CPF: '))
            dia = int(input('Dia de nascimento: '))
            mes = int(input('Mês(1-12): '))
            ano = int(input('Ano de nascimento: '))
            nascimento= datetime.date(ano,mes,dia)
            profissao = str(input('Profissão: '))
            cliente = Cliente(nome,cpf,nascimento,profissao,'Cliente')
            registro[cpf] = cliente 
            nConta = random.randint(100,999)
            if nConta in cCorrente:
                nConta = random.randint(100,999)
            saldo = 100               
            corrente = ContaCorrente(nConta,cliente,saldo,'Conta Corrente')
            cCorrente[nConta] = corrente
            print('Conta criada com sucesso!')

def listarCorrente():
    for chave, i in cCorrente.items():
        i.listar()  

def conta_Poupanca():
    total = 0
    nConta = random.randint(100,999)
    if nConta in cPoupanca:
        nConta = random.randint(100,999)
    saldo = 0
    poupanca = ContaPoupanca(nConta,saldo,cliente,'Conta Poupança',total) 
    cPoupanca[nConta] = poupanca
    print('Conta criada com sucesso!')

def cadastrar_contaPoupanca():
    cont = 0
    print('\tCadastrar Conta Poupança:')
    cpf = str(input('CPF: '))
    for i in cPoupanca.values():
        cont = i.verificar(cpf)

    if cont == 0:
            nome = str(input('Nome: '))
            #cpf = str(input('CPF: '))
            dia = int(input('Dia de nascimento: '))
            mes = int(input('Mês(1-12): '))
            ano = int(input('Ano de nascimento: '))
            nascimento= datetime.date(ano,mes,dia)
            profissao = str(input('Profissão: '))
            cliente = Cliente(nome,cpf,nascimento,profissao,'Cliente')
            registro[cpf] = cliente 
            conta_Poupanca() 
    else:
            print('Não é possivel criar uma conta desse tipo')

def listarPoupanca():
    for chave, i in cPoupanca.items():
        i.listar()

def criarSeguro():
    total = 0
    valorMensal = 0
    valorTotal = 0
    cpf = str(input('Cpf: '))
    for i in registro.keys():  
        if i == cpf:
            lista = []
            cliente2 = registro[cpf]
            if cpf in segVida.keys():
                valorMensal = float(input('Valor mensal do seguro: '))
                valorTotal = valorMensal * 12
                seguroVida = SeguroDeVida(cliente2,valorMensal,valorTotal,total)
                segVida[cpf].append(seguroVida)
            else:
                
                valorMensal = float(input('Valor mensal do seguro: '))
                valorTotal = valorMensal * 12
                seguroVida = SeguroDeVida(cliente2,valorMensal,valorTotal,total)
                lista.append(seguroVida)
                segVida[cpf] = lista
                                
                for chave,i in segVida.items():
                    print('\n',i,'\n')
                print('Seguro de vida criado com susesso!')
        else:
            print('cliente não cadastrado no sistema')

def imprimirHistorico():
    opc = int(input('1-Conta Corrente\n2-Conta Poupança '))
    if opc == 1:
        listarCorrente()
        num = int(input('Número da conta: '))
        if num in cCorrente.keys():
            cCorrente[num].imprimirHistorico()
        else:
            print('Conta não encontrada!')
    if opc == 2:
        listarPoupanca()
        num = int(input('Número da conta: '))
        if num in cPoupanca.keys():
            cPoupanca[num].imprimirHistorico()
        else:
            print('Conta não encontrada!')

def idade(ano,mes,dia):
    anoAtual = datetime.date.today()
    idade = anoAtual.year - ano
    if anoAtual.month < mes:
        idade-=1
    return idade

          
if __name__ == "__main__":

    print('\t1-Cadastar Funcionário\n\t2-Cadastrar Cliente\n\t3-Cadastrar Conta Corrente\n\t4-Cadastrar Conta Poupança\n\t5-Listar\n\t6-Seguro de vida\n\t7-Operações\n\t8-sair')
    esc = int(input('Selecione a opção desejada: '))
    while esc != 8:
        if esc ==8:
            print('sistema finalizado')
            break
        if esc == 1:
            nome = str(input('Nome: '))
            cpf = str(input('CPF: '))
            if cpf in registro:
                print('Cpf já cadstrado')
            dia = int(input('Dia de nascimento: '))
            mes = int(input('Mês(1-12): '))
            ano = int(input('Ano de nascimento: '))
            nascimento= datetime.date(ano,mes,dia)
            salario = float(input('Salário: '))
            funcionario = Funcionario(nome,cpf,nascimento,salario,'Funcionário')
            registro[cpf] = funcionario
        if esc == 2:
            nConta = 0
            total = 0
            nome = str(input('Nome: '))
            cpf = str(input('CPF: '))
            dia = int(input('Dia de nascimento: '))
            mes = int(input('Mês(1-12): '))
            ano = int(input('Ano de nascimento: '))
            id = idade(ano,mes,dia)
            if id < 16:
                print('Não é possivel criar uma conta')
                break
            nascimento= datetime.date(ano,mes,dia)
            profissao = str(input('Profissão: '))
            cliente = Cliente(nome,cpf,nascimento,profissao,'Cliente')
            cliente2 = Cliente(nome,cpf,nascimento,profissao,'')
            registro[cpf] = cliente
            print('\tCriar Conta:\n\t1-Conta Corrente\n\t2-Conta Poupança')
            op = int(input('Selecione a opç desejada:'))
            if op == 1:
                total = 0
                nConta = random.randint(100,999)
                if nConta in cCorrente:
                    nConta = random.randint(100,999)
                saldo = 0               
                corrente = ContaCorrente(nConta,cliente,saldo,'Conta Corrente',total)
                cCorrente[nConta] = corrente
                print('Conta criada com sucesso!')

            if op == 2:
               conta_Poupanca()

        if esc == 3:
            cadastrar_ContaCorrente()
        if esc == 4:
            cadastrar_contaPoupanca()  
        if esc == 5:
            op = int(input('1-Listar Correntes\n2-Listar Poupanças\n3-Listar todas '))
            if op == 1:
                listarCorrente()
            if op == 2:
                listarPoupanca()
            if op == 3:
                listarCorrente()
                listarPoupanca()
        if esc == 6:
            criarSeguro()
        if esc == 7:
            op = int(input('1-Sacar\n2-Depositar\n3-Transerir\n4-Histórico\n5-Calcular tributação\n6-Banco '))
            if op == 1:
                opc = int(input('1-Conta Corrente\n2-Conta Poupança '))
                if opc == 1: 
                    listarCorrente()
                    numero = int(input('Conta: '))
                    valor = float(input('Valor: '))
                    for chave, i in cCorrente.items():
                        i.sacar(numero,valor)
                if opc == 2:
                    listarPoupanca()
                    numero = int(input('Conta: '))
                    valor = float(input('Valor: '))
                    for chave, i in cPoupanca.items():
                        i.sacar(numero, valor)
            if op == 2:
                opc = int(input('1-Conta Corrente\n2-Conta Poupança '))
                if opc == 1:
                    listarCorrente()
                    numero = int(input('Conta: '))
                    valor = float(input('Valor: '))
                    for chave, i in cCorrente.items():
                        i.depositar(numero,valor)
                if opc == 2:
                    listarPoupanca()
                    numero = int(input('Conta: '))
                    valor = float(input('Valor: '))
                    for chave, i in cPoupanca.items():
                        i.depositar(numero, valor)
            if op == 3:
                opc = int(input('1-Conta Corrente\n2-Conta Poupança '))
                if opc == 1:
                    origem = int(input('Conta de origem: '))
                    valor = float(input('Valor da transferencia: '))
                    destino = int(input('Conta de destino: '))
                    for chave, i in cCorrente.items():
                        i.transferir(origem, valor,destino)
                if opc == 2:
                    origem = int(input('Conta de origem: '))
                    valor = float(input('Valor da transferencia: '))
                    destino = int(input('Conta de destino: '))
                    for chave, i in cPoupanca.items():
                        i.transferir(origem, valor,destino)
            if op ==4:
                imprimirHistorico()
            if op == 5:
                totalTributos = 0
                at = Tributacao(totalTributos)
                at.tributa(corrente) 
            if op == 6:
                cont = 0
                cont2 = 0
                for  i in cCorrente.values():
                    cont = i.totalcontas()
                for i in cPoupanca.values():
                    cont2 = i.totalcontas()
                totall = cont+cont2
                print('\nTotal de Registros realizados:')
                tot = len(registro)
                for i in registro.values():
                    print(i,'\n')
                print(f'Total: {tot}')
                print('Contas: ')
                listarCorrente()
                listarPoupanca()
                print(f'Total de Contas no Banco: {totall}')
                print('Seguros de Vida: ')
                c=0
                for i in segVida.values():
                    for x in i:
                        c +=1
                        print('\n',x,'\n')
                print(f'Total Seguros de Vida: {c}')

                #teste()


                    
        esc = int(input('Selecione a opção desejada: '))
    
