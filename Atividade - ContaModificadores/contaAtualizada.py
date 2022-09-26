from Conta import *
import random
registro={}
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
        conta = Conta(nConta,cliente,saldo)
        registro[nConta] = conta

    if esc ==2:
        for chave, i in registro.items():
            i.listar()
    
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
        valor = float(input('Vaor: '))
        destino = int(input('Conta destino'))
        for chave, i in registro.items():
            i.transfere(origem,valor,destino)
    if esc == 7:
        conta.historico.imprimir()
    esc = int(input('Digite a opc: '))


    