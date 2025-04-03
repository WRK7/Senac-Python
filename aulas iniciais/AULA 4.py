# print ("-------------LISTAS------------")

''' X = "Ederson"

 y = ["Edersonn", 18, 23.5]

 print (y) '''

# Pelo o que eu entendi, listas são uma forma de agrupar dados já transformados em variavéis. Mas tenho que rever isso melhor.

'''lista1 = ["Kaio", "Douglas", "José", "Philip"]
lista2 = [12,34,33,22,6321,435431,43,1]

print (type(lista1))

print (lista1,lista2)'''

# Você pode fazer listas de um único tipo de variavél ou de varios tipos


'''lista3 = [12,34,56, 10 + 10, ["Pablo", "Jhonson", "TMFW", "Kaleb"]]

print (lista3)'''

# Pode-se fazer sublistas, que é quando você adiciona uma lista dentro da outra (Professor falou que isso é mais visto em matrizes)
# Também é possível realizar calculos dentro das listas

'''lista4 = [12,34,56, 10, "Pablo", "Jhonson", "TMFW", "Kaleb"]
lista5 = [12,34,56, 10, ["Pablo", "Jhonson", "TMFW", "Kaleb"]]

print (len(lista4))
print (len(lista5))'''

# o len() pode ser usado para contar a quantidade de elementos dentro de uma lista, mas ele não conta a quantidade de elementos dentro de uma sub lista, ele conta a sublista inteira como um elemento

'''lista6 = [12,34,56, 10, "Pablo", "Jhonson", "TMFW", "Kaleb"]

print (lista6[6])
print (lista6[-2])
print (lista6[3-2])''' # isso faz o calculo do índice e me mostra o elemento no índice do RESULTADO
'''print (lista6[4],lista6[5])''' # Assim foi a única forma até o momento que eu consegui de fazer mostrar dois índices de uma lista

# pode-se pegar um elemento da lista pelo índice

'''lista7 = [12,34,56, 10, "Pablo", "Jhonson", "TMFW", "Kaleb"]

print (lista7[4][1])'''

# nessa situação, o primeiro índice mostra o ítem da lsita, o segundo mostra o elemento do item

'''lista8 = [12,34,56, 10, "Pablo", ["Jhonson", "TMFW"], "Kaleb"]

print (lista8[5][0][3])'''

# nessa situação, ele vai imprimir o elemento no índice dentro do item dentro da sublista, no caso, o "n" de "Jhonson"

'''frutas = ["abacaxi", "mamão", "pera", "maça", "abacate", "limão", "pepeino", "laranja", "bergamota", "manga", "banana", "jaca", "guarana", "Pequi", "pocã", "maxixe", "amora", "cereja", "tutifruti", "uva",]

print ("maxixe" in frutas)
print ("Picles" in frutas)'''

# Esse aqui é para identificar um item especifico dentro da lista


'''frutas1 = ["abacaxi", "mamão", "pera", "maça", "abacate", "limão", "pepeino", "laranja", "bergamota", "manga", "banana", "jaca", "guarana", "Pequi", "pocã", "maxixe", "amora", "cereja", "tutifruti", "uva",]

print ([1,2]+[3,4])
print (frutas1 + [5,6,7])
print ([] * 4)
print ([1,2,["ola,adeus"]]*2)'''

# apenas concatena em uma única lista (não entendi muito bem, então se vira ai)

'''a = [1,2,3,4,5,6,7,232,345,32,55,2222,454,-2,-6,7,12]


print (a)
print (max(a))
print (min(a))
print (sum(a))'''

# aqui ele mostra o maior número, menor e a soma de tudo

# OBS: DEPOIS FAZER COM LETRA E LETRA EM NÚMERO

'''a = [1,2,3,4,5,6,7,232,345,32,55,2222,454,-2,-6,7,12]

print (a[1:4]) # é do local indicado até o índice
print (a[:4]) #é do zero até o índice
print (a[3:]) # é do terceiro índice ao além
print (a[:]) #mostra tudo
print (a[0:6]) #normal'''

# OBS, O ULTIMO VALOR DO ÍNDICE NÃO É CONTADO (dá um play que você vai entender, seu burro)

