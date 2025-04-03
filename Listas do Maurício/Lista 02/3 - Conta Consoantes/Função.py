def contar(texto):
    consoante = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z','B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'W', 'Z']   # lista das consoantes
    contador = 0  # contador zerado
    for i in texto:   # mapeia todos as letras dentro do "texto"
        if i in consoante:   # Compara as letras anteriores com os consoantes da lista, e caso hava algum, soma o contador em mais um
            contador += 1

    return contador



