import math  # Biblioteca para cálcular a raiz quadrada

def desvio_padrao(lista):
    if len(lista) == 0:  # Caso especial: lista vazia
        raise ValueError("A lista não pode estar vazia.")

    # Passo 1: Calcular a média
    media = sum(lista) / len(lista)

    # Passo 2: Calcular as diferenças ao quadrado
    somatorio = sum((x - media) ** 2 for x in lista)

    # Passo 3: Calcular a média das diferenças ao quadrado
    variancia = somatorio / len(lista)

    # Passo 4: Retornar a raiz quadrada da variância (desvio padrão)
    return math.sqrt(variancia)






