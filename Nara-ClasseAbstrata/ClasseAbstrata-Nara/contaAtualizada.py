from Conta import *
import random
registro={}

def listarContas():
    if len(registro) == 0:
        print('Não há contas registradas.')
    else:
        for chave, i in registro.items():
            i.listar()

def imprimirHistorico():
    num = int(input('Número da conta: '))
    if num in registro.keys():
        registro[num].imprimirHistorico()
    else:
        print('Conta não encontrada!')

def excluirConta():
    numero = int(input('Conta: '))
    if numero in registro.keys():
        del registro[numero]
    
print('1-Criar Conta\n2-Listar Contas\n3-Sacar\n4-Depositar\n5-Excluir\n6-Transferir\n7-Histórico\n8-Sair')
esc = int(input('Digite a opc: '))
i =0
while esc != 8:
    if esc == 8:
        break
    if esc == 1:
        nome = str(input('Nome: '))
        sobrenome = str(input('Sobrenome: '))
        cpf = str(input('CPF: '))
        saldo = 0
        nConta = random.randint(100,999)
        cliente = Cliente(nome,sobrenome,cpf)
        op = int(input('\t1-Poupança\n\t2-Corrente\n\t3-Investimento'))
        if op == 1:
            contaP = ContaPoupanca(nConta,cliente,saldo,'Conta Poupança')
            registro[nConta] = contaP
            if True:
                print('Conta criada com sucesso')
        elif op == 2:
            contaC = ContaCorrente(nConta,cliente,saldo,'Conta Corrente')
            registro[nConta] = contaC
            if True:
                print('Conta criada com sucesso')
        elif op == 3:
            contaIn = ContaInvestimento(nConta,cliente,saldo,'Conta Investimento')
            registro[nConta] = contaIn
            if True:
                print('Conta criada com sucesso')
    if esc ==2:
        listarContas()  
    if esc == 3:
        numero = int(input('Conta: '))
        valor = float(input('Vaor: '))
        for chave, i in registro.items():
            i.sacar(numero,valor)
    if esc == 4:
        numero = int(input('Conta: '))
        valor = float(input('Vaor: '))
        for chave, i in registro.items():
            i.depositar(numero,valor)
    if esc == 5:
        excluirConta()
    if esc ==6:
        origem = int(input('Conta de origem: '))
        valor = float(input('Valor: '))
        destino = int(input('Conta destino'))
        for chave, i in registro.items():
            i.transfere(origem,valor,destino)
    if esc == 7:
        imprimirHistorico()
            
    esc = int(input('Digite a opc: '))


    