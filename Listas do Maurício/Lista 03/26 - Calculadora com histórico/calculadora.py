# 26. Classe Calculadora com Histórico:
# Crie uma classe Calculadora com um histórico de operações realizadas.


class Calculadora ():
    def __init__ (self,valor1:float,valor2:float):
        self.valor1 = valor1
        self.valor2 = valor2
        self.historico = []
    def Somar (self):
        print (self.valor1 + self.valor2)
        historicos = ({self.valor1}, '+' ,{self.valor2})
        self.historico.append(historicos)
        print (self.historico)
    def Subtrair (self):
        print (self.valor1 - self.valor2)
        historicos = ({self.valor1}, '-' ,{self.valor2})
        self.historico.append(historicos)
        print (self.historico)
    def Dividir (self):
        print (self.valor1 / self.valor2)
        historicos = ({self.valor1}, '/' ,{self.valor2})
        self.historico.append(historicos)
        print (self.historico)
    def Multiplicar (self):
        print (self.valor1 * self.valor2)
        historicos = ({self.valor1}, '*' ,{self.valor2})
        self.historico.append(historicos)
        print (self.historico)
    




