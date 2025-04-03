
class ControleRemto:
    def __init__(self,cor,altura,profundidade,largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        self.canais = ['globo','sbt','record','cartoonnetwork']
        self.contador = -1
    def MudarCanal (self,botao):
        if botao=='+':
                self.contador +=1
                if self.contador > 3:
                    self.contador = 0
                laranja = self.canais[self.contador]
                print (laranja)
        elif botao=='-':
            self.contador -=1
            if self.contador < 0:
                self.contador = 0
            laranja = self.canais[self.contador]
            print (laranja)
        else:
            print ('Valor Invalido')



controle1 = ControleRemto('preto',23,45,54)
controle1.MudarCanal('+')
controle1.MudarCanal('-')
controledoquarto4 = ControleRemto('preto',16,6,5)
controledoquarto4.MudarCanal('-')
controledoquarto3 = ControleRemto('azul',11,3,9)
controledoquarto3.MudarCanal('+')
controledoquarto2 = ControleRemto('cinza',18,2,5)
controledoquarto2.MudarCanal('+')
controledoquarto1 = ControleRemto('vermelho',19,7,2)
controledoquarto1.MudarCanal('-')
controleremotodasala = ControleRemto('verde',10,5,3)
controledoquarto1.MudarCanal('p')