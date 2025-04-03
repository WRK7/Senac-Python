def multiplica_pares(lista):
    produto = 1  # Inicializa o acumulador de multiplicação
    tem_par = False  # Flag para verificar se há pares na lista

    for numero in lista:
        if numero % 2 == 0:  # Verifica se o número é par
            produto *= numero
            tem_par = True  # Marca que há pelo menos um par

    return produto if tem_par else 0  # Retorna o produto ou 0 se não houver pares
