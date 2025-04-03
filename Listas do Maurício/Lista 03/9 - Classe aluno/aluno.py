# Crie uma classe Aluno com atributos nome e nota. Adicione um método que exiba se o
# aluno está aprovado (nota >= 7).

class Aluno:
    def __init__ (self,nome,nota):
        self.nome = nome
        self.nota = nota
    
    def CalculoDeAprovação (self):
        if self.nota >= 7:
            print ('Aprovado')
        else:
            print ('Reprovado')