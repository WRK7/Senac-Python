n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = ((n1 + n2) /2)
if (media <= 4):
    print (f"Nota: E \nNota 1: {n1}\n Nota 2: {n2}\nMédia: {media}\nREPROVADO")
elif (media >= 4.1 and media <= 5.9):
    print (f"Nota: D \nNota 1: {n1}\n Nota 2: {n2}\nMédia: {media}\nREPROVADO")
elif (media >= 6 and media <= 7.5):
    print (f"Nota: C \nNota 1: {n1}\n Nota 2: {n2}\nMédia: {media}\nAPROVADO")
elif (media >= 7.6 and media <= 9):
    print (f"Nota: B \nNota 1: {n1}\n Nota 2: {n2}\nMédia: {media}\nAPROVADO")
elif (media >= 9.1 and media <= 10):
    print (f"Nota: A \nNota 1: {n1}\n Nota 2: {n2}\nMédia: {media}\nAPROVADO")