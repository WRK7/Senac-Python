class Ponto:
    def __init__ (self,X,Y):
        self.X = X
        self.Y = Y
    def Valores (self):
        print (self.X)
        print (self.Y)

class Retangulo:
    def __init__ (self,Largura,Altura):
        self.Largura = Largura
        self.Altura = Altura
    def Alterar (self):
        self.Largura = int(input("Digite a nova Largura: "))
        self.Altura = int(input("Digite a nova Altura: "))
    def Centro (self):
        self.resultado1 = self.Largura/2
        self.resultado2 = self.Altura/2
        print (self.resultado1)
        print (self.resultado2)
        
