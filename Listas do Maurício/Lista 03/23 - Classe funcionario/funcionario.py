# 23. Classe Funcionário:
# Crie uma classe Funcionario com os atributos nome e salario. Adicione um método
# para calcular um aumento de salário.


class Funcionario():
    def __init__ (self,nome:str,salario:float):
        self.nome = nome
        self.salario = salario
    def Aumento (self):
        print (f'O salário atual de {self.nome} é de R${self.salario}')
        aumento = float(input(f'Digite de quanto será o aumento de {self.nome}: '))
        return print (f'Agora o novo salario de {self.nome} é de R${aumento + self.salario}')
        

    