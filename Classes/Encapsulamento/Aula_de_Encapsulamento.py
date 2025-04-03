class Encapsulamento():
    def __init__ (self,num1,num2):
        self.__num1 = num1
        self.__num2 = num2
    def adicionar (self):
        return self.__num1 + self.__num2
    def subtrair (self):
        return self.__num1 - self.__num2
    
calc = Encapsulamento(20,10)
print (calc.adicionar())
print(calc.__num1) 

#os dois underscore encapsulam (__)

#=============================================

#Saída esperada: AttributeError: 'Encapsulamento' object has no attribute '__num1'

class Encapsulamento():
    def __init__ (self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def __adicionar (self):
        return self.num1 + self.num2
    def subtrair (self):
        return self.num1 - self.num2
    
calc = Encapsulamento(20,10)
print (calc.adicionar())
 
#Serve para qualquer objeto