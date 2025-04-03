class Tamagoshi:
    def __init__ (self,nome:str,fome:str,saude:str,idade:int):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
    def Humor (self):
        if self.fome == 'Não' and self.saude == 'Boa':
            print (f'O {self.nome} está feliz!')
        elif self.fome == 'Sim' and self.saude == 'Ruim':
            print (f'O {self.nome} está triste!')
        else:
            print ('Valores incompreendidos ou invalidos!')
            
    def AlterarNome (self):
        self.nome = input('Digite o novo nome: ')
    def AlterarFome (self):
        self.fome = input(f'Digite se o {self.nome} está com fome (Use "Sim" ou "Não"): ')
    def AlterarSaude (self):
        self.saude = input(f'Digite como está a saúde do {self.nome} (Use "Boa" ou "Ruim"): ')
    def AlterarIdade (self):
        self.idade = int(input('Digite a nova idade do {self.nome}: '))

