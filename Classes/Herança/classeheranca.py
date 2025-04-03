class Account():
    def __init__ (self,number: int,holder: str,balance:float):
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit (self):

        deposito = float(input("digite o deposito: "))
        self.balance = self.balance + deposito
        print (self.balance)

    def withdraw (self):
        saque = float(input("digite o saque: "))
        if saque <= self.balance:
            self.balance = self.balance - saque
            print (self.balance)
        else:
            print ("Saldo Insuficiente!")
        


#++++++++++++++++++++++++++++++

class AccountBussines(Account):
    def __init__(self, number: int, holder: str, balance: float, loanlimit: float):
        super().__init__(number, holder, balance)
        self.loanlimit = loanlimit
    def loan(self,amount: float):
        if amount <= self.loanlimit:
            self.balance = self.balance + amount

            self.loanlimit = self.loanlimit - amount

            print (f'Foi adicionado o valor de R${amount} a sua conta.\nVocê agora tem R${self.balance} em sua conta.\nVocê tem apenas R$ {self.loanlimit} para empréstimo disponível.')
        else:
            print ('Você não pode sacar tudo isso')



#++++++++++++++++++++++++++++++




accountbussines = AccountBussines(2,'Wesley',10,2000)
accountbussines.loan(200)
accountbussines.deposit()
accountbussines.withdraw()