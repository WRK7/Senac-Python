# 28. Classe Banco:
# Crie uma classe Banco que contenha várias ContaBancaria. Adicione um método para
# listar os saldos de todas as contas.


class Banco():
    def __init__ (self,conta1:float,conta2:float,conta3:float,conta4:float,conta5:float):
        self.conta1 = conta1
        self.conta2 = conta2
        self.conta3 = conta3
        self.conta4 = conta4
        self.conta5 = conta5
        self.lista = []    
    def Listar (self):
        self.lista.append(self.conta1)
        self.lista.append(self.conta2)
        self.lista.append(self.conta3)
        self.lista.append(self.conta4)
        self.lista.append(self.conta5)
        return print(self.lista)

