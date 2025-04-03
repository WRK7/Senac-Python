n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = ((n1 + n2 + n3 + n4) /4)

if (media == 10):
    print ("Aprovado com Distinção")
    print (f"Suas notas são {n1}, {n2}, {n3}, {n4} e sua média é {media}")
elif (media >= 7 ):
    print ("Aprovado")
    print (f"Suas notas são {n1}, {n2}, {n3}, {n4} e sua média é {media}")
elif (media < 7):
    print ("Reprovado")
    print (f"Suas notas são {n1}, {n2}, {n3}, {n4} e sua média é {media}")