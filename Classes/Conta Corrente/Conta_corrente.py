class Conta_Corrente:
    def __init__(self,NumeroDaConta,NomeDoCorrentista,Saldo):
        self.NumeroDaConta = NumeroDaConta
        self.NomeDoCorrentista = NomeDoCorrentista
        self.Saldo = Saldo
    def AlterarNomes (self):
        self.NomeDoCorrentista = input("Digite o novo nome do correntista: ")        
    def MostrarNome (self):
        return self.NomeDoCorrentista
    def Saque (self):
        saque = float(input("Digite quando quer sacar: "))
        self.Saldo = self.Saldo - saque
        print (self.Saldo)
    def Deposito (self):
        deposito = float(input('Digite quanto você quer '))
        self.Saldo = deposito - self.Saldo
        print (self.Saldo)
        
