def absoluta (lista):
    lista_nova = []
    if len(lista) < 2:
        return []

    for i in lista:
        diferença = [abs(lista[i + 1] - lista[i]) for i in range(len(lista) - 1)]
    

    return diferença