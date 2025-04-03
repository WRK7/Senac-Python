# 12. Classe Filme:
# Crie uma classe Filme com os atributos titulo e duracao. Adicione um método para
# exibir os detalhes.



class Filme():
    def __init__ (self,titulo:str,duracao:str):
        self.titulo = titulo
        self.duracao = duracao
    def Detalhes (self):
        return print (f'O título do filme é {self.titulo}\nA duração é de {self.duracao}')

