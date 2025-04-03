'''class Conta():
    def __init__ (self,nome,saldo,cpf,senha):
        self.nome = nome
        self.__saldo = saldo
        self.__cpf = cpf
        self.__senha = senha
    def Depositar (self,saldo):
        self.deposito = float(input('Digite o quanto quer depositar: '))
        self.__saldo = saldo + self.deposito
        print ("O valor já foi depositado em sua conta") #talvez precise de um retunr ao inves de um print
    def Extrato (self,senha):
        # self.senhaverificada = int(input('Digite a senha: '))
        if self.__senha == senha:
            return print(self.__saldo)
        else:
            print ('Senha incorreta!')
    def Sacar (self,senha):
        if self.__senha == senha:
            self.saque = float(input('Digite o quanto quer sacar: '))
            self.__saldo = self.__saldo - self.saque
            print (self.__saldo)
        else:
            print ('Senha incorreta!')
    def Dados (self):
        return print (self.nome,self.__saldo,self.__cpf,self.senha)'''


class Conta():
    def __init__(self, nome, saldo, cpf, senha):
        self.nome = nome
        self.__saldo = saldo
        self.__cpf = cpf
        self.__senha = senha

    def Depositar(self, saldo):

            self.deposito = float(input('Digite o quanto quer depositar: '))
            if self.deposito > 0.50:
                self.__saldo = saldo + self.deposito
                print("O valor já foi depositado em sua conta")
            else:
                print("Erro: Por favor, digite um valor numérico válido para o depósito.")

    def Extrato(self, senha):
        try:
            if self.__senha == senha:
                return print(self.__saldo)
            else:
                print('Senha incorreta!')
        except Exception as e:
            print(f"Erro inesperado ao acessar o extrato: {e}")

    def Sacar(self, senha):
        try:
            if self.__senha == senha:
                self.saque = float(input('Digite o quanto quer sacar: '))
                if self.saque > self.__saldo:
                    print("Erro: Saldo insuficiente.")
                else:
                    self.__saldo = self.__saldo - self.saque
                    print(f"Novo saldo: {self.__saldo}")
            else:
                print('Senha incorreta!')
        except ValueError:
            print("Erro: Por favor, digite um valor numérico válido para o saque.")
        except Exception as e:
            print(f"Erro inesperado ao tentar sacar: {e}")

    def Dados(self):
        try:
            return print(self.nome, self.__saldo, self.__cpf, self.__senha)
        except Exception as e:
            print(f"Erro ao acessar os dados: {e}")



conta1 = Conta('Pablo',0,'xxxxx',1)
conta1.Depositar(0)