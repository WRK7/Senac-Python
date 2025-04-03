while True:
    valor = int(input("Digite um, valor entre 0 e 10 "))
    if (valor < 0 and valor > 10):
        print ("Tente de novo!")
    elif (valor >= 0 and valor <= 10):
        print ("Parabéns")
        break