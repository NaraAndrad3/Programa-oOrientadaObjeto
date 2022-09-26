import random
registro ={}
class Conta:
    def __init__(self,nome,conta,saldo):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo
    def listar(self):
        print('Nome: {}\nConta: {}\nSaldo:{}\n'.format(self.nome, self.conta,self.saldo))
    
    def sacar(self,numero,valor):
        if numero == self.conta:
            self.saldo -=valor
        #print('saldo de atual: R${}'.format(self.saldo))
    
    def depositar(self,numero,valor): 
        if numero == self.conta:
            self.saldo+=valor
        #print('saldo de atual: R${}'.format(self.saldo))
    def excluir(self,numero):
        if numero in registro.keys():
            del registro[numero]
        else:
            print('Conta inválida')
            
        
print('\tMENU')
print('1-Criar Conta\n2-Listar Contas\n3-Sacar\n4-Depositar\n5-Excluir\n6-sair')
esc = int(input('Digite a opc: '))
while esc!=6:
    if esc ==6:
        break
    if esc ==1:
        conta = random.randint(100,999)
        nome = str(input('Nome: '))
        saldo = 0
        print('Nome: {} Conta: {} Saldo: {}'.format(nome,conta,saldo))
        pessoa=Conta(nome,conta,saldo)
        registro[conta] = pessoa
        conta = 0
        saldo =0
        op = int(input('Adicionar conta?(1-Sim 2-Não)'))
        while op != 2:
            if op ==2:
                break
            if op ==1:
                conta = random.randint(100,999)
                nome = str(input('Nome: '))
                saldo = 0
                print('Nome: {} Conta: {} Saldo: {}'.format(nome,conta,saldo))
                pessoa=Conta(nome,conta,saldo)
                registro[conta] = pessoa
            op = int(input('Adicionar conta?(1-Sim 2-Não)'))
    
    if esc == 2:
        for chave, i in registro.items():
            i.listar()
    if esc ==3:
        numero = int(input('Conta: '))
        valor = float(input('Valor: '))
        for chave, i in registro.items():
            i.sacar(numero,valor)
    if esc ==4:
        numero = int(input('Conta: '))
        valor = float(input('Valor: '))
        for chave,i in registro.items():
            i.depositar(numero,valor)
    if esc ==5:
        
        for chave, i in registro.items():
            i.listar()
            numero = int(input('Conta: '))       
    esc = int(input('Digite a opc: '))    










 