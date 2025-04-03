gasolina = 2.50
alcool = 1.90
escolha = input("Escolha\n1 - Gasolina\n2- Álcool\n")
if (escolha == "1"):
    litrosg = int(input("Quantos Litros de GASOLINA sera adicionado:"))
    if (litrosg <= 20):
        amor = litrosg * gasolina
        totalg = ((amor * 0.04) - amor)
        print (f"Você tera que pagar R${totalg}")
    elif (litrosg > 20):
        amor = litrosg * gasolina
        totalg = ((amor * 0.06) - amor)
        print (f"Você tera que pagar R${totalg}")
if (escolha == "2"):
    litrosa = int(input("Quantos Litros de ÁLCOOL sera adicionado:"))
    if (litrosa <= 20):
        amor = litrosa * alcool
        totala = (( amor * 0.03) - amor)
        print (f"Você tera que pagar R${totala}")
    elif (litrosa > 20):
        amor = litrosa * alcool
        totala = ((amor * 0.05) - amor )
        print (f"Você tera que pagar R${totala}")