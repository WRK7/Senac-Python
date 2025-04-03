def ocorrencia(texto):
    ocorrencia = {}
    palavra = texto.split()
    
    for palavras in palavra:
        ocorrencia[palavras] = ocorrencia.get(palavras,0)+1
    return ocorrencia
    
print(ocorrencia('Olá Olá'))

# josé que ensinou (e eu ainda não entendi)