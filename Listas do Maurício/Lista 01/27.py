def elementos_unicos(lista):
    unicos = []
    for elemento in lista:
        if lista.count(elemento) == 1:
            unicos.append(elemento)
    return unicos

lista = [4,5,6,7,8,9,9,9,2,2,3,4,1,1,1,4]
print(elementos_unicos(lista))


#josé que ensinou (e eu ainda não entendi)