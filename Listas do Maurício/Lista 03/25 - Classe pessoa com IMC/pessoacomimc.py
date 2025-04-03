# 25. Classe Pessoa com IMC:
# Crie uma classe Pessoa com atributos altura e peso. Adicione um método para calcular
# o IMC (peso / altura2).


class Pessoa ():
    def __init__ (self,altura:float,peso:float):
        self.altura = altura
        self.peso = peso
    
    def Imc (self):
        return print (self.peso/(self.altura**2))


