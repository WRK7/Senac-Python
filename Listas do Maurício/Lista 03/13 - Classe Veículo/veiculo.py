# 13. Classe Veículo:
# Crie uma classe Veiculo com atributos modelo e velocidade. Adicione um método para
# aumentar a velocidade.

class Veículo():
    def __init__ (self,modelo:str,velocidade:int):
        self.modelo = modelo
        self.velocidade = velocidade
    def AumentarVelocidade (self,velocidade):
        self.velocidade = velocidade + self.velocidade
        return print(f'Velocidade ajustada para {self.velocidade}km/h')

