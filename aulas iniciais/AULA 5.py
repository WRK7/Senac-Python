# Listas mutaveis

'''frutas = ["bananas","pera","maça"]


frutas[0] = "maça"
frutas[-1] = "banana"

print (frutas)'''

#essa é uma forma de mudar as ordem da lista (não funciona em apenas trings)

'''frutass = ["bananas","pera","maça"]


frutass[0] = "maça"
frutass[-2] = "banana"

print (frutass)'''

#não reajusta automaticamente

'''uma_lista = ['a','b','c','d','e','f']
uma_lista[1:3] = ['x','y']

print (uma_lista)'''

# Forma de adicionar vários elementos em uma lista


'''mais_uma_lista = ['a','b','c','d','e','f']
print (mais_uma_lista)
print (len(mais_uma_lista))



mais_uma_lista[1:3] = []
print (mais_uma_lista)
print (len(mais_uma_lista))'''

# Uma forma de remover elementos da lista, não é a melhor, mas estamos aprendendo ela porque ela existe (palavras do professor)

'''uma_listaa = ['a','d','f']
print (uma_listaa)
uma_listaa[1:1] = ['b','c']
print (uma_listaa)
uma_listaa[4:4] = ['e']
print (uma_listaa)'''


# Essa é uma das formas de adicioanr elementos, mas elas espremem para o lado, então se deve colocar exatamente a posição (ex: [1:1], [5:5], [132:132])


'''lista = [1,2,3,4]

del lista[2]
print (lista)

listaa = [1,2,3,4,5,6,7,8,9,10]
del listaa[3:7]
print (listaa)'''

# Essa é a forma mais simples de deletar elementos de uma lista que o próprio python oferece "del[posição]"


# ================Operador . (ponto) - append==================


'''lista_a = [81,82,83]

lista_a.append(5)

print (lista_a)'''

# Essa é uma forma de adicioanr, ela é chamada de "Fila" ou "Ilha" pois todo elemento que ela adiciona, vai para o final da fila


'''listaaa = [1,5,2,3,5,6,1,23,4,6,8,5,43,32,1,2,3,4,65,7,8,9,1,2,3,4,5,6,7,8,9,10]

listaaa.sort()

print (listaaa)

# Esse comando organiza os valores, em número ele sempre coloca em ordem crescente, e em ordem alfabética

listat = ["w","e","s","l","e","y"]
listat.sort()

print (listat)

listaa = [1,5,2,3,5,6,1,23,4,6,8,5,43,32,1,2,3,4,65,7,8,9,1,2,3,4,5,6,7,8,9,10]

listaa.sort (reverse=True) # Esse comando inverte a ordem

print (listaa)'''


'''lista = [1,2,3,4,5,6,7,8,9,10]

print (lista.index(3))'''

# Esse mostra em qual índice da lista está certo elemento (ele só mostra o primeiro, se tivessem nove "3" ele mostraria apenas o primeiro)


'''lista = [1,3,5,7,9]

lista.insert(1,2) 

print (lista)

lista2 = ["W","s","l","e","y"]

lista2.insert(1,"e")

print (lista2)'''

# O primeiro é o índice, e o segundo é o elemento




'''lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 5, 9, 0, 0, 1, 5, 2, 6, 5, 8, 9, 7, 9, 1, 0, 3, 7, 1, 4, 0, 2, 9, 6, 5, 3, 5, 2, 8, 1, 6, 5, 4, 3, 8, 4, 6, 2, 7, 1, 4, 0, 9, 5, 2, 6, 1, 3, 5, 8, 7, 9, 0, 0, 2, 7, 4, 1, 6, 8, 3, 2]

print (lista.count(1))'''


# Esse "count" serve para contar quantas vezes um determinado elemente aparece na lista


'''lista = [71,72,73,74,75,76,77,78]

lista.pop() # Quando vazio, apaga o último elemento da lista
print (lista)

lista.pop(0) # Mas você pode definir o índice de qual você quer apagar
print (lista)

lista.pop(-1)
print (lista)'''


lista = [1,2,3,[4,5,6]]

lista.extend([4,5,6])

print (lista)
