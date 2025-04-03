# Crie uma classe Temperatura com um método para converter graus Celsius para
# Fahrenheit.


class Temperatura:
    def __init__(self,Celsius):
        self.Celsius = Celsius
    def Conversão (self):
        return self.Celsius * 1.6 + 32
    