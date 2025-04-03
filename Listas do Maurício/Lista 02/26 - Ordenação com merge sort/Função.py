def merge_sort(lista):
    if len(lista) <= 1:  # Caso base: lista com 0 ou 1 elemento já está ordenada
        return lista
    
    # Divisão da lista ao meio
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])  # Ordena a primeira metade
    direita = merge_sort(lista[meio:])   # Ordena a segunda metade

    # Função para mesclar as duas listas ordenadas
    return mesclar(esquerda, direita)

def mesclar(esquerda, direita):
    resultado = []  # Lista para armazenar o resultado
    i = j = 0

    # Mesclando as listas enquanto houver elementos em ambas
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adicionando os elementos restantes (se houver)
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado
