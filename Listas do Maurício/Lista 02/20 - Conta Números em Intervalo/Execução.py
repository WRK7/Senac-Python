from Função import *




lista = [3, 7, 2, 9, 5, 8, 4]

# Intervalo a ser analisado
inicio = 4
fim = 8

# Chamada da função
resultado = conta_intervalo(lista, inicio, fim)
print(f"Quantidade de números no intervalo [{inicio}, {fim}]: {resultado}")
# Saída esperada: 4 (números: 7, 5, 8, 4)
