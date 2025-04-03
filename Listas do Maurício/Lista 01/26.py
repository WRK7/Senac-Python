def soma_pares(lista):
    lista_duplicado = []
    lista_duplicado2 = []
    for elemento in lista:
        if elemento not in lista_duplicado:
            lista_duplicado.append(elemento)
        else:
            lista_duplicado2.append(elemento)
    return sum(lista_duplicado2)
        
        
    
        
lista = [4,5,6,7,8,9,9,9,2,2,3,4,1,1,1,4]
print(soma_pares(lista))

#josé que ensinou (e eu ainda não entendi)