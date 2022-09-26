class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, funcionario):
        self._total_bonificacoes += funcionario.get_bonificacao()

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes




        '''''
        
        lass AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total
    @property
    def selic(self):
        return self._selic
    @selic.setter
    def selic(self,taxa):
        self._saldo_total = taxa
    @property
    def saldoTotal(self):
        return self._saldo_total
    @saldoTotal.setter
    def saldoTotal(self,valor):
        self._saldo_total = valor

    def registra(self,conta):
        print('Saldo atual: {}'.format(conta._saldo))
        self._saldo_total = conta.atualiza()
        self._saldo = self.
        
        
        
        '''