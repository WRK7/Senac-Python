# ====== LAÇO DE REPETIÇÃO========
#========== WHILE ==============

'''a = 10

while (a<20): # é usado igual o enquanto do portugol. (enquanto a for menor que 100)
    print ("menor")
    a = a +1 # contador que soma mais um
print ("fim")'''

# ==========

'''while True: #Esse comando causa um loop infinito sem que precise
    print ("Loop Infitino")'''


'''while True:
    valor = int(input("Digite 1 ou 0 para fim "))
    if valor == 1:
        print ("Valor correto")
    else: 
        print ("Valor para sair")
        break # O break para apenas o while em que está '''

'''while True:
    while True:
        valor = int(input("Digite 1 ou 0 para fim "))
        if valor == 1:
            print ("Valor correto")
        else: 
            print ("Valor para sair")
            break
# nesse caso, ele para apenas o segundo while, o break nunca quebra o código '''

#=============

while True:
    valor = int(input("Digite o valor 1 ou 0 para encerar"))
    if valor >=1:
        continue # o continue faz com que o while retorne ao começo
        print ("TESTE")
    if valor >=1:
        print ("Teste 2")

