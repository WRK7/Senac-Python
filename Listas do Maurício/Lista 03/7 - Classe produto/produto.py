# Crie uma classe Produto com os atributos nome e preço. Adicione um método para
# aplicar um desconto ao preço.



class Produto:
    def __init__ (self,nome,preço):
        self.nome = nome
        self.preço = preço
    
    def DescontoPreço (self):
        return (self.preço-((self.preço*10)/100))
    
