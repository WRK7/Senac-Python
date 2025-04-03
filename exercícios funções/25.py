def remove(lista):
    lista_de_duplicados = []
    for elemento in lista:
        if elemento not in lista_de_duplicados:
            lista_de_duplicados.append(elemento)
    return lista_de_duplicados
        
        
    
        
lista = [4,5,6,7,8,9,9,9,2,2,3,4,1,1,1,4]
print(remove(lista))


#josé que ensinou (e eu ainda não entendi)