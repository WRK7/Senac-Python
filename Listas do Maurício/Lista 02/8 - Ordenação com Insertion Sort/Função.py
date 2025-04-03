def insertion_sort(lista):
    # Percorre os elementos a partir do segundo
    for i in range(1, len(lista)):
        # O elemento a ser inserido
        chave = lista[i]
        j = i - 1

        # Move os elementos maiores que a chave uma posição para a direita
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        # Insere a chave na posição correta
        lista[j + 1] = chave

    return lista

# não entendi nada disso, tenho que estudar melhor

