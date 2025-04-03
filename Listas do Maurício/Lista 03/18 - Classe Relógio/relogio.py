# 18. Classe Relógio:
# Crie uma classe Relogio com os atributos hora, minuto e segundo. Adicione um
# método para exibir o horário no formato HH:MM


class Relógio():
    def __init__ (self,hora:int,minuto:int,segundo:int):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    def Hora (self):
        return print (f"As horas são {self.hora}:{self.minuto}")
    
