def multiplica(lista,escalar):

    nova_lista = [] #lista vazia
    
    
    for elemento in lista:  # o "elemento" vai percorrer a "lista"
        
        resultado = elemento * escalar  # o "elemento" vai multiplicar pelo escalar, cada valor da lista, um a um, e salvar na variavel "resultado"
        
        nova_lista.append(resultado) # o resultado sera adicionado na "nova_lista"
        
    return nova_lista