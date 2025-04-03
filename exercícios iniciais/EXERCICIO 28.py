salario = float(input("Digite o salário: "))

if (salario <= 280 ):
    salarior = (((salario * 20) / 100) + salario)
    print (f"Seu salário antes do ajuste era de R${salario}")
    print ("O percentual aumentado é de 20%")
    print ("O valor do aumento é de R$",salario - salarior)
    print (f"Seu salário após o ajuste é de R${salarior}")
elif (salario >= 280 and salario <= 700):
    salarior = (((salario * 15) / 100) + salario)
    print (f"Seu salário antes do ajuste era de R${salario}")
    print ("O percentual aumentado é de 15%")
    print ("O valor do aumento é de R$",salario - salarior)
    print (f"Seu salário após o ajuste é de R${salarior}")
elif (salario >= 700 and salario <= 1500):
    salarior = (((salario * 10) / 100) + salario)
    print (f"Seu salário antes do ajuste era de R${salario}")
    print ("O percentual aumentado é de 10%")
    print ("O valor do aumento é de R$",salario - salarior)
    print (f"Seu salário após o ajuste é de R${salarior}")
elif (salario >= 1500):
    salarior = (((salario * 5) / 100) + salario)
    print (f"Seu salário antes do ajuste era de R${salario}")
    print ("O percentual aumentado é de 5%")
    print ("O valor do aumento é de R$",salario - salarior)
    print (f"Seu salário após o ajuste é de R${salarior}")
    