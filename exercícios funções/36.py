def perfeito (n):
    lista = []
    for i in range (1,n):  #percorre de um valor até o número decidido
        if(n%i==0):  #enquanto percorre vai dividindo o valor decidido por todos os número percorridos
            lista.append(i) #os que dão resto zero representado por "%", vão sendo salvos na lista vazia

    if (n== sum(lista)): #soma os valores salvos na lista para serem somados e entregar o resultado
        return ("é perfeito")
    else:
        return 'não é perfeito'


print (perfeito(10))


#José ajudou

