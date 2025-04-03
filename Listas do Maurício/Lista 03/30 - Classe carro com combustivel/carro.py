# 30. Classe Carro com Combustível:
# Crie uma classe Carro com os atributos marca e combustivel. Adicione métodos para
# abastecer e verificar o nível de combustível.


class Carro ():
    def __init__ (self,marca:str,combustivel:str):
        self.marca = marca
        self.combustivel = combustivel
        self.medido = [0,10,20,30,40,50,60,70,80,90,100]
        self.contador = combustivel
    def Abastecer (self):
        if self.contador >= 10:
            print ('O tanque já está cheio!')
        else:
            self.contador += 1
            medido2 = self.medido[self.contador]
            return medido2
    
    def Verificar (self):
        if self.contador >= 10:
            print ('O tanque já está cheio!')
        elif self.contador >= 0:
            elemento = self.medido[self.contador]
            print (f'O se nivel de combustivel está em {elemento}%')
        else:
            print (f'han? {self.combustivel} sério??')
    


