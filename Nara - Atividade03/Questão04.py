class Televisao:
    def __init__(self,volume =0,canal=1):
        self._volume = volume
        self._canal = canal
    
    @property
    def mostrarCanal(self):
        return self._canal

    @mostrarCanal.setter
    def mostrarCanal(self,channel):
        self._canal = channel
    
    @property
    def mostrarVol(self):
        return self._volume
    
    @mostrarVol.setter
    def mostrarVol(self,vol):
        self._volume = vol

class ControleRemoto:
    
    def __init__(self,tv=Televisao()):
        self.tv = tv
 
    def aumentarVolume(self):
        print('O volume atual: {}'.format(self.tv._volume))
        self.tv._volume +=1
        print('O volume atual: {}'.format(self.tv._volume))
    def diminuirVolume(self):
        print('O volume atual: {}'.format(self.tv._volume))
        self.tv._volume-=1
        print('O volume atual: {}'.format(self.tv._volume))
    def aumentarCanal(self):
        print('O canal atual: {}'.format(self.tv._canal))
        self.tv._canal +=1
        print('O canal atual: {}'.format(self.tv._canal))
    def diminuirCanal(self):
        print('O canal atual: {}'.format(self.tv._canal))
        self.tv._canal -=1
        print('O canal atual: {}'.format(self.tv._canal))
    def escolherCanal(self):
        print('O canal atual: {}'.format(self.tv._canal))
        canal = int(input('Digite o numeroo do canal: '))
        self.tv._canal = canal
        print('O canal atual: {}'.format(self.tv._canal))
    def canalAtual(self):
        print(f'O canal atual é: {self.tv._canal}\nO volume da TV é: {self.tv._volume}')

controle=ControleRemoto()
print('\t1-Aumenar Volume\n\t2-Diminuir Volume\n\t3-Aumentar Canal\n\t4-Diminuir Canal\n\t5-Escolher Canal\n\t6-Mostrar\n\t0-Desligar')
esc = int(input('Digite: '))
while esc !=0:
    if esc==0:
        print('Televisão desligada!')
        break
    if esc ==1:
        controle.aumentarVolume()
    if esc == 2:
        controle.diminuirVolume()
    if esc ==3:
        controle.aumentarCanal()
    if esc == 4:
        controle.diminuirCanal()
    if esc ==5:
        controle.escolherCanal()
    if esc == 6:
        controle.canalAtual()
    esc = int(input('Digite: '))




    







