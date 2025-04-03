class Retangulo:
    def __init__ (self,ladoA,ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def Pedir (self,ladoA,ladoB):
        self.ladoA = float(input("Digite o lado A: "))
        self.ladoB = float(input("Digite o lado B: "))
        return print (self.ladoA, self.ladoB)
    def Area (self):
        return self.ladoA*self.ladoB
    def Perimetro (self):
        return ((self.ladoA*2) + (self.ladoB*2))