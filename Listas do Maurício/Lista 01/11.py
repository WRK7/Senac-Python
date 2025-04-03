def palavras(texto):
    lista = texto.split()
    return len(lista)
    
texto = 'José babão paia'
print(palavras(texto))