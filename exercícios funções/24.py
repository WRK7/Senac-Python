def conta_ocorrencia(lista, elemento):
    cont = 0
    for i in range (0, len(lista)):
        if(lista[i] == elemento):
            cont = cont+1
        
    return cont
lista = [4,5,6,7,8,9,9,9,2,2,3,4,1,1,1,4]
print(conta_ocorrencia(lista, 1))



#josé que ensinou (e eu ainda não entendi)