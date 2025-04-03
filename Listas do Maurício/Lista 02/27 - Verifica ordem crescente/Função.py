def esta_ordenada(lista):
    for i in range(len(lista) - 1):  # Percorre até o penúltimo elemento
        if lista[i] > lista[i + 1]:  # Se o elemento atual for maior que o próximo
            return False  # A lista não está ordenada
    return True  # A lista está ordenada
