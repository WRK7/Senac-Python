# 21. Classe Livro com Estoque:
# Adicione à classe Livro um atributo para controlar a quantidade em estoque.

class Livro():
    def __init__ (self,escolha:int):
        self.escolha = escolha
    def Controle (self):
        escolha = int(input('Qual livro você quer procurar? Veja as nossas opções\n1-Senhor dos Aneis\n2-Trono de Vidro\n3-Morro dos Ventos uivantes\nDigite aqui a sua escolha: '))
        if escolha == 1:
            print ('Acabou o estoque desse livro!')
        elif escolha == 3:
            print ('Restam menos de 10 livros no estoque')
        elif escolha == 2:
            print ('Tem uma boa quantidade desse livro nos estoques')

