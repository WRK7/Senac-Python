# 17. Classe Data:
# Crie uma classe Data com os atributos dia, mes e ano. Adicione um método para
# formatar a data no estilo DD/MM/AAAA.


class Data():
    def __init__ (self,dia:int,mes:int,ano:int):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def FormatarData (self):
        return print (f'A data de hoje é {self.dia}/{self.mes}/{self.ano}')

