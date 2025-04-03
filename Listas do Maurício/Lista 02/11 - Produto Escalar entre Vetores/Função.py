def escalar(vetor1, vetor2):
    # Verifica se os vetores têm o mesmo tamanho
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo tamanho.")

    # Calcula o produto escalar
    produto = sum(a * b for a, b in zip(vetor1, vetor2))  #zip organiza em pares
    return produto



