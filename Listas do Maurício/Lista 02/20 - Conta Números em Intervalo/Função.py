def conta_intervalo(lista, inicio, fim):
    # Validar se inicio é menor ou igual a fim
    if inicio > fim:
        raise ValueError("O início do intervalo deve ser menor ou igual ao fim.")
    
    contador = 0  # Contador para números no intervalo

    for numero in lista:
        if inicio <= numero <= fim:  # Verifica se o número está no intervalo
            contador += 1

    return contador
