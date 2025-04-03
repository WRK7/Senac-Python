print ("Digite seu nome")
nome = input ()
print (nome)

# o print serve como o leia do portugol, mas ele recebe apenas strings (textos), porém tem como mudar isso

print ("------------------------")


nome = input ("Digite seu nome")
print (nome)

# também pode ser feito assim

print ("------------------------")



idade = input ("Digite sua idade")
print (type(idade))

# Prova de que o input apenas vai sempre considerar aquilo dentro dele como string

print ("------------------------")

salario = int(input('Salario?'))
print (salario)
imposto = float(input('imposto?'))
print (imposto)

# Usamos aquela formula para decidir se o input sera para inteiro ou real

print ("----------------------")

sal = float(input("Digite seu salário"))
print (sal) 
print ("O salário digitado foi %f" % (sal))

print ("Eu tenho um filho de %d anos, outro de %d anos, e outro de %d anos" % (10, 23, 25))

z = 1724/111

print ("%.2f" % z)
print ("%.4f" % z)


# tenha fé que você vai se lembrar (PLACEHOLDER)
# tentativa de explicar: essa porcentagem serve para você colcoar um valor dentro da linha de código que fica após o parenteses, ele lê por ordem primaria

w = "Wesley Chato"

print(f"{w}")

# Celso mostrou que serve para mostrar textos de uma variavél, ams tem que estar dentro das chaves


f1 = int(input("filho 1"))
f2 = int(input("Filho 2"))
f3= int(input("Filho 3"))

print ("Eu tenho um filho de %d anos, outro de %d anos, e outro de %d anos" % (f1, f2, f3))

# serve com input também

# COLINHA DO SIGNIFICADO DE CADA PORCENTAGEM
# %d = inteiro
# %s = string
# %f = float
# %b = bool


print ("----------------------")



#CONCATENAÇÃO

a = "Ederson"
b = "Costa"


print ("Prezado "+a+" "+b+". "+"Olá")

# Junta texto. Imagina que ele comprime todo um texto em um pequeno elemento

print ("----------------------")

#CONCATENAÇÃO

a = "Ederson"
b = "Costa"


print ("Prezado "+a+" "+b+". "+"Olá")

# Junta texto. Imagina que ele comprime todo um texto em um pequeno elemento

print ("Prezado %s %s. Olá" % (a, b))

print ("----------------------")


print (10* "Ederson\n")

# Isso aqui repete o texto diversas vezes (conforme a quantidade pedida)
#desafio proprio (fazer isso com input pra definir quantas vezes sera repetido)


print ("------------------------------")


print ("+" + 10* "-" + "+")
print (("|"+" "*10 + "|\n") *5, end="")
print ("+" + 10* "-" + "+")


print ("+" + 15* "-" + "+")
print (("|" +" " *15 + "|\n") *4, end="")
print ("+" + 15* "-" + "+")


print (5* " " + "/\\" + 5* " ")
print (4* " " + "/" + 2* " " + "\\" + 5* " ")
print (3* " " + "/" + 4* " " + "\\" + 5* " ")
print (2* " " + "/" + 6* " " + "\\" + 5* " ")
print (1* " " + "/" + 8* "-" + "\\" + 5* " ")


# desafio do professor

print ("------------------------")




2

frase = "um triangulo de base igual a {0} e altura igual a {1} possui area igual a {2}.".format(3,4,12)

print (frase)


# isso é a forma de formatação de string mais avançada (parecido com o que o Celso ensinou, mas agora tem variaveis)

# segue uma ordem, onde 0 é a posição 1, 1 é a posição 2, e 2 é a posição 3

print ("----------------------")





linguagem = "python"

frase = (f"programando em (linguagem)")

print (frase)

#forma mais facil de tratar a variavel string


print ("----------------")

x = (2/3)
print(f"printando o {x}")
print (f" printando o {x:.2f}")

#forma mais facil de tratar a variavel float (real)

("------FIM DA AULA 2------")