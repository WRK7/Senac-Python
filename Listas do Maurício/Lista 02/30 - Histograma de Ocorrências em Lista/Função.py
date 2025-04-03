def histograma(lista):
    ocorrencias = {}  # Dicionário para armazenar as ocorrências
    for elemento in lista:
        if elemento in ocorrencias:
            ocorrencias[elemento] += 1  # Se o elemento já está no dicionário, incrementa
        else:
            ocorrencias[elemento] = 1  # Se não está no dicionário, adiciona com valor 1
    return ocorrencias
