v1 = int(input("Escreva um valor: "))
v2 = int(input("Escreva um outro valor: "))
v3 = int(input("Escreva mais um valor: "))
#considere um programa para ler três valores inteiros (considere que não serão lidos valores iguais) e escreve-los em ordem crescente


if (v1 > v2 and v2 > v3):
    print (v3,v2,v1)
elif (v3 > v2 and v2 > v1):
    print (v1,v2,v3)
elif (v1 > v3 and v3 > v2):
    print (v2,v3,v1)
elif (v1 > v3 and v3 > v2):
    print (v1,v3,v2)
else:
    print (v2,v1,v3)