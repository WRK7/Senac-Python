'''print ("------------MANIPULAÇÃO DE STRINGS-------------")'''

'''a = "Wesley"

print(len(a))'''

# o comando "len()" serve para contar a quantidade de elementos em uma string (não tem áspas fora)

'''b = len(a)

print (b)'''

# pode-se atribuit o len() para uma variavél

'''print ("-------------------CAPITALZE-------------")'''

'''c = "wesley"

print (c.capitalize())'''

#deixa em maiúsculo a primeira letra

'''print ("-------------------UPPER-------------")'''

'''d = "wesley"

print(d.upper())'''

# esse deixa tudo em maiúsculo

'''print ("-------------------CASEFOLD-------------")'''


'''e = "WESLEY"

print(e.casefold())'''

# esse deixa tudo em minúsculo

'''print("wesley".upper())'''

# também pode-se aplicar o texto diretamente sem o uso de uma variavél (isso so aplica aos outros passados)

'''print ("-------------------LOWER-------------")'''


'''f = "WESLEY"

print (f.lower())

print ("WESLEY".lower())'''

# essa faz a mesma coisa da ultima

'''print ("-------------------ISLOWER-------------")'''


'''g = "wesley"

print(g.islower())

h = "Wesley"

print(h.islower())'''

# Esse serve para dizer se o conteúdo é minúsculo ou maiúsculo. true é minuscúlo e false é maiúsculo


'''print ("-------------------ISUPPER-------------")'''


'''i = "wesley"

print(i.isupper())

j = "WESLEY"

print(j.isupper())'''

'''print ("-------------------ISDIGIT-------------")'''


'''k = "1234"

print (k.isdigit())

l = "1234asd"

print (l.isdigit())'''

# esse serve para mostrar se tem apenas números INTEIROS

'''print (type(int(k)))'''

# pode-se declara o valor por uma variavel inteiro

'''print ("-------------------REPLACE-------------")'''



'''m = "wesley gomes"


print (m.replace("gomes","cruz"))'''
               #Original #outro


# esse substitui um elemento do string original por outro


'''print ("-------------------SPLIT-------------")'''

'''n = "Wesley da Cruz Gomes"

print (n.split(" "))

o = "Wesley-da-Cruz-Gomes"

print (o.split("-"))'''


# Esse split separa os objetos espaçados, seja o puro espaço ou substituindo um elemento

'''print ("-------------------FIND-------------")'''


'''p = "Wesley da Cruz Gomes"

print (p.find("u"))'''

# Esse identifica a posição/índice onde está uma letra ou palavra, ele trás apenas o primeiro elemento. (A contagem sempre começa do 0)


'''print ("-------------------IN-------------")'''


'''q = "Wesley da Cruz Gomes"

print ("Cruz"in(q))

r = "Wesley da Cruz Gomes"

print ("picles"in(r))'''


# serve para dizer se existe a letra ou palavra em umna variavél

'''print ("-------------------count-------------")'''


'''s = "Wesley da Cruz Gomes"

print (s.count("e"))'''

# Essa mostra quantas vezes em uma variavél aparece deteminado número de letras ou palavras

'''print ("---------INMANIPULAÇÃO DE STRINGS-SUB STRINGS-------")'''


'''t = "Olá, mundo!"

print(t[0])
print(t[2])
print(t[7])
print(t[1])
print(t[8])'''


# Esse aqui é para te mostrar a letra da string a partir da posição/índice


'''print(t[-5])
print(t[-1])
print(t[-3])'''

# podemos usar valores negativos, eles são contados da direita para esquerda, sendo -1 a última letra

'''print ("-------------------SLICES-------------")'''


u = "Olá, Mundo!"

print(u[4:9])



# Esse corta uma fatia, de um índice ao outro PORÉM, o ultimo índice não é contado, ele é um limitador


'''print ("-------------------SLICES-------------")'''

