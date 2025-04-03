class Bola:
    def __init__ (self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def Troca_Cor (self,cor):
        self.cor = cor
    def Mostrar_Cor (self):
        print (f"A cor da bola é {self.cor}")