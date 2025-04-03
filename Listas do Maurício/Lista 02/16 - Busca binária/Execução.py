from Função import *


# Lista ordenada de exemplo
lista = [1, 3, 5, 7, 9, 11, 13]

# Elemento a ser buscado
elemento = 7

# Chamada da função
indice = busca_binaria(lista, elemento)
print(f"Índice do elemento {elemento}: {indice}")  # Saída esperada: 3

# Teste com elemento não encontrado
elemento_nao_presente = 4
indice_nao_presente = busca_binaria(lista, elemento_nao_presente)
print(f"Índice do elemento {elemento_nao_presente}: {indice_nao_presente}")  # Saída esperada: -1



# :(