def diferencao (lista1,lista2):
    conjunto = set(lista2)

    return [adicionar for adicionar in lista1 if adicionar not in conjunto] 


# o elemento é o conjunto que eu vou adicionar a nova lista, 
# for elemento in lista1 é porque o elemento que vai pra nova lista, 
# ai percorrer toda a lista1 analisando elemento atrás de elemento, 
# e o elemento not in conjunto2 é porque ele vai adicionar o elemento analisado e se não tiver no conjunto2, 
# ele vai adicionar no elemento lá do começo



lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4]

print (diferencao(lista1,lista2))
