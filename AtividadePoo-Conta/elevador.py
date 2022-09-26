class Elevador:
    def __init__(self,andar_atual,andares,capacidade,n_pessoas):
        
        self._andar_atual = andar_atual
        self._andares = andares
        self._capacidade = capacidade
        self._n_pessoas = n_pessoas

    @property
    def andar_atual(self):
        return self._terreo
    @andar_atual.setter
    def andarAtual(self,atual):
        self._andar_atual = atual
    
    @property
    def andares(self):
        return self._andares
    @andares.setter
    def andares(self,total):
        self._andares = total
    
    @property
    def capacidade(self):
        return self._capacidade
    @capacidade.setter
    def capacidade(self,cap):
        self._capacidade = cap
    
    @property
    def n_pessoas(self):
        return self._n_pessoas
    @n_pessoas.setter
    def n_pessoas(self,quant):
        self._n_pessoas = quant

    def inicializa(self,cap,q_andares):
        self._capacidade = cap
        self._andares = q_andares

    def entrar(self):
        if self._n_pessoas == self._capacidade:
            print('Elevador lotado')
        else:
            num = int(input('quantidade: '))
            self._n_pessoas = (self._n_pessoas + num)
            print('Quantidade de pessoas: {}'.format(self._n_pessoas))

    def sair(self):
        if self._n_pessoas > 0:
            num = int(input('Quantidade de pessoas: '))
            self._n_pessoas = (self._n_pessoas - num)
            print('Quantidade de pessoas: {}'.format(self._n_pessoas))

    def subir(self):
        if self._andar_atual == self._andares:
            print('O elevador já se encontra no ultimo andar')
        else:
            self._andar_atual +=1
            print('Andar atual: {}'.format(self._andar_atual))

    def descer(self):
        if self._andar_atual == 0:
            print('O elevador já se encontra no Térreo')
        else:
            self._andar_atual -=1
            print('Andar atual: {}'.format(self._andar_atual))




