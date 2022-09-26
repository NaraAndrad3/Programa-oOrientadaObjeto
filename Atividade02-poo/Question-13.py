global agenda
agenda = {}
def Incluir(nome,tel):
    i=0
    op = int(input('quantas pessoas deseja adiconar á agenda? '))
    for i in range(0,op):#Nota= para usar listas é melhor o for do que o while
        tel=[]
        nome = str(input('Nome: '))
        tel.append(int(input('Telefone: ')))
        esc = int(input('Deseja adicionar mais telefones? (1-Sim 2-Não) '))
        if esc == 1:
            esco = int(input('Quantos? '))
            for i in range(0,esco):
                tel.append(int(input('Telefone: ')))
        else:
            pass
        agenda[nome] = tel
        

def IncluirTelefone(tel):
    nome = str(input('Digite o nome onde incluir o contato: '))
    if nome not in agenda:
        esc = int(input('O nome não conta na agenda, Deseja incluí-lo? (1-Sim 2-Não) '))
        if esc == 1:
            Incluir(nome, tel)
        else:
            print('Você escolheu não incluir')
    else:
        for i in agenda:
            if nome ==i:
                tel.append(int(input('Digite o numero: ')))
                tel=[]

def ExcluirTelefone():
    global agenda
    nome = str(input('Digite o nome da pessoa: '))
    num=int(input('Digite o numero a ser apagado: '))
    if nome in agenda.keys():
        if len(agenda[nome])==1:
            del agenda[nome]
        else:
            for i in range(0,len(agenda[nome])-1):
                if num == agenda[nome][i]:
                    agenda[nome].pop(i)    
            
def ExcluirNome():
    print(agenda.keys())
    key = str(input('Digite o nome a ser excluido da agenda: '))
    agenda.pop(key)          

def ConsultarTelefone():
    nome = str(input('Digite o nome desejado para consulta: '))
    for i in agenda:
        if i == nome:
            print(agenda[nome])
nome =''
tel = [] 
print('1- Incluir novo item\n2-Incluir Telefone\n3-Excluir Telefone\n4-Excluir Nome\n5-Consultar Telefone\n(Digite -1 para sair)')
esc = int(input('Digite a opção desejada: '))
while esc!=-1:
    if esc == 1:
        Incluir(nome,tel)
    elif esc == 2:
        IncluirTelefone(tel)
    elif esc == 3:
        ExcluirTelefone()
    elif esc ==4:
        ExcluirNome()
    elif esc ==5:
        ConsultarTelefone()
    print('1- Incluir novo item\n2-Incluir Telefone\n3-Excluir Telefone\n4-Excluir Nome\n5-Consultar Telefone\n(Digite -1 para sair)')
    esc = int(input('Digite a opção desejada: '))
print(agenda)

