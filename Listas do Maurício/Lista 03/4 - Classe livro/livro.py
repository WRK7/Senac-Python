# Crie uma classe Livro com os atributos titulo e autor. Adicione um método para exibir
# os detalhes do livro.

class Livro:
    def __init__ (self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    def informacoes (self):
        print (self.titulo,self.autor)