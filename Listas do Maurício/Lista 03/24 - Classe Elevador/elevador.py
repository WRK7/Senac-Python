# 24. Classe Elevador:
# Crie uma classe Elevador com atributos andarAtual e totalAndares. Adicione métodos
# para subir e descer.

class Elevador():
    def __init__ (self,andarAtual:0,totalAndares:list):
        self.andarAtual = andarAtual
        self.totalAndares = totalAndares
        self.contador = -1
    def Subir (self,botao):
        if botao != '>':
            print ('O botão para subir o elevador é ">"')
        else:
            if self.contador > 10:
                print ('Você já está no último andar')
            else:
                self.contador += 1
                elemento = self.totalAndares[self.contador]
                return print (elemento)
    def Descer (self,botao):
        if botao != '<':
            print ('O botão para subir o elevador é "<"')
        else:
            if self.contador < 1:
                print ('Você já está no térreo')
            else:
                self.contador -= 1
                elemento = self.totalAndares[self.contador]
                return print (elemento)


