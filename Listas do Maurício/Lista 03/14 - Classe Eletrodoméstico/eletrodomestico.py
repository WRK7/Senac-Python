# 14. Classe Eletrodoméstico:
# Crie uma classe Eletrodomestico com os atributos nome e potencia. Adicione um
# método para ligar o aparelho.


class Eletrodoméstico():
    def __init__ (self,nome:str,potencia:int):
        self.nome = nome
        self.potencia = potencia
    
    def Ligar (self):
        return print(f'Ligando o {self.nome} a {self.potencia} wats de potência')