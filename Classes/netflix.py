class Netflix:
    def __init__(self):
        self.Nome = str
        self.Email = str
        self.Cpf = int
        self.Plano = str
        self.CartãoDeCrédito = int
        self.Fone = int
    
    def Cadastro (self):
        self.Nome = input("Digite seu nome: ")
        self.Email = input("Digite o seu E-Mail: ")
        self.Cpf = int(input("Digite o seu CPF: "))
        self.CartãoDeCrédito = int(input("Digite os números do seu cartão de crédito: "))
        self.Fone = int(input("Digite o seu telefone: "))
        print ("Qual plano deseja?\n1 - Plano Solteiro\n2 - Plano Casal\n3 - Plano Familia")
        self.Plano = input("Digite o plano que você deseja: ")
        
        if self.Plano == "1" or self.Plano == "2" or  self.Plano == "3":
            print (f"Plano escolhido {self.Plano}")
        else:
            print ("Esse plano não existe! >:(")
        
    def Dados (self):
        print (self.Nome,self.Email,self.Cpf,self.CartãoDeCrédito,self.Fone)

úsuario1 = Netflix()
print(úsuario1.Cadastro())
print(úsuario1.Dados())