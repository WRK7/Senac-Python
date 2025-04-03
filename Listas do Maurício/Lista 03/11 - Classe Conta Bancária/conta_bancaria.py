# Classe Conta Bancária:
# Crie uma classe ContaBancaria com os atributos saldo. Adicione métodos para
# depositar e sacar dinheiro.


class Conta_Bancaria():
    def __init__ (self,balance):
        self.balance = balance
    def Depositar(self):
        print (f'Você tem {self.balance}')
        depositar = float(input("Digite o valor que quer depositar: "))
        self.balance = depositar + self.balance
        return print (self.balance)
    def Sacar(self):
        print (f'Você tem {self.balance}')
        sacar = float(input("Digite o valor que quer sacar: "))
        self.balance = sacar + self.balance
        return print (self.balance)

