
nomep = (input("Digite o nome do produto: ")) 
quantidade = int(input("\nAgora digite a quantidade que foi comprada: "))
unidade = float(input("\nAgora digite o valor de cada unidade: "))
desconto = float(input("\nAgora a porcentagem do desconto: "))


total1 = unidade * quantidade
vdesconto = ((total1 * desconto) / 100)
total = total1 - vdesconto
print (f"\nO produto comprado foi: {nomep}\nO valor total foi de: R$ {total1}\nO valor do desconto foi de: R$ {vdesconto:.2f}\nO valor total é de: R$ {total:.2f}")