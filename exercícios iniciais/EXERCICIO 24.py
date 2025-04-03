ma = int(input("Digite quantas maças voc:e vai comprar: "))

if (ma < 12):
    mam = ma * 0.30
    print (f"A compra das suas {ma} maçãs dara o valor de R$",mam)
else:
    man = ma * 0.25
    print (f"A compra das suas {ma} maçãs dara o valor de R$",man)