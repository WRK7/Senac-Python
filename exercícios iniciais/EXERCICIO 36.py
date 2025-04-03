while True:
    while True:
        nome = input("Digite o seu nome: ")
        nomes = len(nome)
        if nomes <= 3:
            print ("NOME: NO MINIMO 3 LETRAS!!")
        else: 
            break
    while True:
        idade = int(input("Digite a sua idade: "))
        if idade < 0 or idade > 150:
            print ("IDADE: ENTRE 0 E 150 ANOS!")
        else:
            break
    while True:
        salario = float(input("Digite seu salário: "))
        if salario < 0:
            print ("SALÁRIO: O SALARIO TEM QUE SER MAIOR QUE ZERO!")
        else: 
            break
    while True: 
        sexo = input("Digite seu sexo como 'm', 'f', ou 'o': ") 
        if sexo != "s" or sexo != "m" or sexo != "o":
            print ("SEXO: APENAS OS SEXOS PEDIDOS!")
        else:
            break
    while True:
        estado = input("Digite seu civil como 's', 'c', 'v' ou 'd': ")
        if estado != "s" or estado != "c" or estado != "v" or estado != "d":
            print ("ESTADO: APENAS OS ESTADOS PEDIDOS!")
        else:
            break
    break