class Quadradro():
    def __init__(self,lado):
        self.Lado = lado
    def area (self):
        return self.Lado**2
    def calculo (self):
        return self.Lado
    
quadradro = Quadradro(2)
print (quadradro.area())
print (quadradro.calculo())