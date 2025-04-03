# Crie uma classe Calculadora com métodos para somar e subtrair dois números.


class Calculadora_Simples:
    def __init__ (self,primeiro_numero,segundo_numero):
        self.primeiro_numero = primeiro_numero
        self.segundo_numero = segundo_numero   
    def Somar(self):
        return self.primeiro_numero + self.segundo_numero
    def Subtrair(self):
        return self.primeiro_numero - self.segundo_numero


