# 22. Classe Agenda:
# Crie uma classe Agenda com um atributo para armazenar contatos e métodos para
# adicionar e listar contatos.


class Agenda():
    def __init__ (self):
        self.contatos = []
    def Adicionar (self):
        contato = input('Adicione o contato: ')
        self.contatos.append(contato)
    def Listar (self):
        return print(self.contatos)

