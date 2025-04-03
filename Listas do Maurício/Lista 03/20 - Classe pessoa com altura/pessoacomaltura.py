# 20. Classe Pessoa com Altura:
# Crie uma classe Pessoa que inclua o atributo altura. Adicione um método para verificar
# se a pessoa é mais alta que 1,75 m.


class Pessoa():
    def __init__ (self,altura:float):
        self.altura = altura
    def Verificar (self):
        if self.altura > 1.75:
            print ('A pessoa tem mais de 1.75')
        elif self.altura == 1.75:
            print ('A pessoa tem exatamente 1.75')
        else:
            print ('A pessoa não tem mais de 1.75')
