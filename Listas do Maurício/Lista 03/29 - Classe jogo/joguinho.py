# 29. Classe Jogo:
# Crie uma classe Jogo com atributos nome e pontuacao. Adicione métodos para iniciar o
# jogo e registrar a pontuação.


class Jogo():
    def __init__ (self,nome:str,pontuacao:float):
        self.nome = nome
        self.pontuacao = pontuacao
    
    def IniciarJogo (self):
        print (f'Iniciando o jogo pi pi po po, zummmmmmmmmmmmmmmm, se prepare {self.nome}!!')
    
    def RegistrarPontuacao (self):
        if self.pontuacao > 1000:
            print (f'Wow {self.nome}, você fez uma pontuação de {self.pontuacao} pontos!')
        elif self.pontuacao < 1000 and self.pontuacao > 1:
            print (f'{self.pontuacao} pontos já é um bom começo {self.nome}!')
        elif self.pontuacao == 0:
            print (f'Você deve ser novo aqui {self.nome}, mas não se desanime! Uma pontuação de {self.pontuacao} pontos é apenas um começo puro')
        else:
            print (f'... {self.nome}, como bulhufas você fez {self.pontuacao} pontos? Isso nem deveria ser possível!')


