def imparpar_lista(lista):
    lista_impar = []
    lista_par = []
    for n in lista:
        if n%2 == 0:
            lista_par.append(n)
        else:
            lista_impar.append(n)

    return lista_par , lista_impar