# 27. Classe Animal com Movimento:
# Crie uma classe Animal com um método mover que imprima uma mensagem
# indicando como ele se move (exemplo: "O peixe nada").


class Animal():
    def __init__ (self):
        self.nada = []
    def Mover (self):
            escolha = input('escolha o animal\n1-Peixe\n2-Cavalo\n3-Gavião\n:')
            if escolha == '1':
                 print ('O Peixe nada')
            elif escolha == '2':
                 print ('O Cavalo anda e corre')
            elif escolha == '3':
                 print ('O Gavião voa')
            else:
                 print ('Ops, parece que não temos essa opção de animal XD')