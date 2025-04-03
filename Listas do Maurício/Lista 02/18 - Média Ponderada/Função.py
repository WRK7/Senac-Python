def media_ponderada(lista_valores, lista_pesos):
    if len(lista_valores) != len(lista_pesos):
        raise ValueError("As listas de valores e pesos devem ter o mesmo tamanho.")

    # Passo 2: Calcular o somatório ponderado
    somatorio_ponderado = sum(v * p for v, p in zip(lista_valores, lista_pesos))

    # Passo 3: Calcular a soma dos pesos
    soma_pesos = sum(lista_pesos)

    if soma_pesos == 0:
        raise ValueError("A soma dos pesos não pode ser zero.")

    # Passo 4: Calcular a média ponderada
    return somatorio_ponderado / soma_pesos
