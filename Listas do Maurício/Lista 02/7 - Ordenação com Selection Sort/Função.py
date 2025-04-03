def selection_sort(lista):
    n = len(lista) #conta a quantidade de elementos na lista (serve para contar os indices que serão usados no "n")
    
    for mn in range(n - 1): #percorre toda a lista menos o ultimo elemento
        menor = mn #adiciona toda a sequencia em uma variavel

        for nm in range(mn + 1,n): #analisa o resto da lista (ultimo elemento)
            if lista[nm] < lista[menor]: #se o ultimo elemento for menor que todo o resto....
                menor = nm #adiciona o novo elemento inferior a variavel antiga

        if menor != mn: #se o novo valor menor for diferente do valor antigo (resto da lista)
            lista[mn], lista[menor] = lista[menor], lista[mn] # trocamos a ordem






# não entendi nada disso, tenho que estudar mais