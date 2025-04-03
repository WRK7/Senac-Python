import math

def numeros_primos(n):
    primos = []  # Lista para armazenar números primos

    for i in range(2, n + 1):  # Verifica números de 2 até n
        # Verifica se i é primo
        is_primo = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_primo = False
                break
        
        if is_primo:
            primos.append(i)  # Adiciona o número primo à lista
    
    return primos
