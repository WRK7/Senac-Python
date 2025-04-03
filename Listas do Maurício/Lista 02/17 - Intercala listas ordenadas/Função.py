def intercala_listas_ordenadas(lista1, lista2):
    i, j = 0, 0  # Índices para percorrer as listas
    resultado = []  # Lista resultante

    # Intercalar enquanto houver elementos em ambas as listas
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Adicionar os elementos restantes de cada lista
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])

    return resultado
