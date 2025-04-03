def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2  # Calcula o índice do meio

        # Verifica se o elemento está no meio
        if lista[meio] == elemento:
            return meio  # Retorna o índice onde o elemento foi encontrado

        # Ajusta os limites com base na comparação
        elif lista[meio] < elemento:
            inicio = meio + 1  # Busca na metade direita
        else:
            fim = meio - 1  # Busca na metade esquerda

    return -1  # Elemento não encontrado
