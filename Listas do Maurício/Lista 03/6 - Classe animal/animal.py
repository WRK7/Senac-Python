# Crie uma classe Animal com os atributos espécie e som. Adicione um método que
# imprima o som do animal.



class Animal():
    def __init__(self,espécie,som):
        self.espécie = espécie
        self.som = som
        
    def OuvirSom(self):
        print (self.som)
        

