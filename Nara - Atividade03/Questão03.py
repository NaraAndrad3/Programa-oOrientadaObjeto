class Elevador:
    def __init__(self,andar_atual,andares,capacidade,n_pessoas):    
        self._andar_atual = andar_atual
        self._andares = andares
        self._capacidade = capacidade
        self._n_pessoas = n_pessoas
    #ENCAPSULAMENTO
    @property
    def andarAtual(self):
        return self._andar_atual
    @andarAtual.setter
    def andarAtual(self,andar):
        self._andar_atual = andar
    
    @property
    def andares(self):
        return self._andares 
    @andares.setter
    def andares(self,andar):
        self._andares = andar
    
    @property
    def capacidade(self):
        return self._capacidade
    @capacidade.setter
    def capacidade(self,capacity):
        self._capacidade = capacity
    
    @property
    def n_pessoas(self):
        return self._n_pessoas
    @n_pessoas.setter
    def n_pessoas(self,quant):
        self._n_pessoas = quant

    #MÉTODOS DA CLASSE
    def inicializar(self,capacidade,andares):
        self._capacidade = capacidade
        self._andares = andares

    def entrar(self):
        if self._n_pessoas == self._capacidade:
            print('Elevador lotado')
        else:
            n = int(input('Quantidade de pessoas: '))
            self._n_pessoas +=n
            print(f'Numero de pessoas: no elevador: {self._n_pessoas}')

    def sair(self):
        if self._n_pessoas == 0:
            print('Não há pessoas.')
        else:
            n = int(input('Quantidade de pessoas: '))
            self._n_pessoas -=n
            print(f'Numero de pessoas: no elevador: {self._n_pessoas}')

    def subir(self):
        n=1
        if self._andar_atual == self._andares:
            print('O elevador já sen encontra no ultimo andar.')
        else:
            self._andar_atual +=n
            print(f'Andar atual: {self._andar_atual}')

    def descer(self):
        n = 1
        if self._andar_atual == 0:
            print('O elevador já se encontra no térreo.')
        else:
            self._andar_atual -=n
            print(f'Andar atual: {self._andar_atual}')

#MAIN
andar_atual = 0
andares = 5
capacidade = 10
n_pessoas = 0
elevador = Elevador(andar_atual, andares, capacidade, n_pessoas)

print('\tMENU\n\t1-Entrar\n\t2-Sair\n\t3-Subir\n\t4-Descer')
esc = int(input('Digite: '))
while esc !=0:
    elevador.inicializar(capacidade,andares)
    if esc == 0:
        break
    if esc == 1:
        elevador.entrar()
    if esc ==2:
        elevador.sair()
    if esc ==3:
        elevador.subir()
    if esc ==4:
        elevador.descer()

    esc = int(input('Digite: '))