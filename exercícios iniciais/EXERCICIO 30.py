p1 = input("Telefonou para a vítima?\n")
p2 = input("Esteve no local do crime?\n")
p3 = input("Mora perto da vítima?\n")
p4 = input("Devia para a vítima?\n")
p5 = input("Já trabalhou com a vítima?\n")
contador = 0
if (p1 == "sim"):
    contador = contador +1
if (p2 == "sim"):
    contador = contador +1
if (p3 == "sim"):
    contador = contador +1
if (p4 == "sim"):
    contador = contador +1
if (p5 == "sim"):
    contador = contador +1
print (contador)
if (contador == 2):
    print ("Suspeita")
elif (contador == 3 or contador == 4):
    print ("Cúmplice")
elif (contador == 5):
    print ("Assassino")
else: 
    print ("Inocente")