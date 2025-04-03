a = int(input("Digite a quatidade de população A: "))
taxx1 = float(input("Digite a taxa de crescimento do país A: "))
b = int(input("Digite a quatidade de população B: "))
taxx2 = float(input("Digite a taxa de crescimento do país B: "))
ano = 0
while a <= b:
    taxa1 = a*taxx1/(100)
    a = a+taxa1
    taxa2 = b*taxx2/(100)
    b = b+taxa2
    ano += 1
print (ano)

