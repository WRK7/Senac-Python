def diagonais_matriz(matriz):
    n = len(matriz)  # Número de linhas (ou colunas, já que é quadrada)

    # Verificar se é uma matriz quadrada
    if any(len(linha) != n for linha in matriz):
        raise ValueError("A matriz deve ser quadrada.")

    diagonal_principal = []
    diagonal_secundaria = []

    # Percorrer a matriz
    for i in range(n):
        diagonal_principal.append(matriz[i][i])  # Elemento da diagonal principal
        diagonal_secundaria.append(matriz[i][n - i - 1])  # Elemento da diagonal secundária

    return [diagonal_principal, diagonal_secundaria]
