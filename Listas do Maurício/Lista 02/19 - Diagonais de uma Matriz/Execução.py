from Função import *



matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Chamada da função
resultado = diagonais_matriz(matriz)
print("Diagonal Principal:", resultado[0])  # Saída esperada: [1, 5, 9]
print("Diagonal Secundária:", resultado[1])  # Saída esperada: [3, 5, 7]
