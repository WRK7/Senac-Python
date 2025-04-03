def quick_sort(lista):
    # Caso base: lista com 0 ou 1 elemento já está ordenada
    if len(lista) <= 1:
        return lista

    # Escolha do pivô (neste caso, o último elemento)
    pivô = lista[-1]

    # Particionamento
    menores = [x for x in lista[:-1] if x <= pivô]  # Elementos menores ou iguais ao pivô
    maiores = [x for x in lista[:-1] if x > pivô]   # Elementos maiores que o pivô

    # Recursão e combinação
    return quick_sort(menores) + [pivô] + quick_sort(maiores)



#eu não entendi nada disso, tenho que estudar muito mais