while True:
    escolha = (input("1 - Multiplicação\n2 - Divisão\n3 - Adição\n4 - Subtração\n5 - Parar\n",))
    if escolha == "1":
        multi = float(input("Escolha o primeiro valor: ")) 
        multi2 = float(input("Escolha o valor por qual quer multiplicar: "))
        print ("resultado: ", multi * multi2)
    elif escolha == "2":
        divi = float(input("Escolha o primeiro valor: ")) 
        divi2 = float(input("Escolha o valor por qual quer dividir: "))
        print ("resultado: ", divi / divi2)
    elif escolha == "3":
        soma = float(input("Escolha o primeiro valor: ")) 
        soma2 = float(input("Escolha o valor por qual quer somar: "))
        print ("resultado: ", soma + soma2)
    elif escolha == "4":
        subt = float(input("Escolha o primeiro valor: ")) 
        subt2 = float(input("Escolha o valor por qual quer subtrair: "))
        print ("resultado: ", subt - subt2)
    else:
        break
print("Saindo...")