from classeheranca import Account

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