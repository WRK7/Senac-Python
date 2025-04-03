# 16. Classe Pessoa com Cumprimento:
# Crie uma classe Pessoa com um método para cumprimentar outra pessoa (imprimir
# "Olá, [nome]").

class PessoaComCumprimento():
    def __init__ (self,nome:str):
        self.nome = nome
    def Cumprimentar (self):
        return print (f'Olá, {self.nome}')
    