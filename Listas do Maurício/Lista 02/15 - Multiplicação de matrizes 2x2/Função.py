def multiplica_matrizes(matriz1, matriz2):
    # Verificar se ambas as matrizes são 2x2
    if len(matriz1) != 2 or len(matriz1[0]) != 2 or len(matriz2) != 2 or len(matriz2[0]) != 2:
        raise ValueError("As matrizes devem ser 2x2.")

    # Elementos da primeira matriz
    a, b = matriz1[0]
    c, d = matriz1[1]

    # Elementos da segunda matriz
    e, f = matriz2[0]
    g, h = matriz2[1]

    # Cálculo dos elementos da matriz resultante
    return [
        [a * e + b * g, a * f + b * h],
        [c * e + d * g, c * f + d * h]
    ]


# Meu Deus do céu! o que é isso?!

# Matrizes de exemplo
matriz1 = [
    [1, 2],
    [3, 4]
]

matriz2 = [
    [5, 6],
    [7, 8]
]



