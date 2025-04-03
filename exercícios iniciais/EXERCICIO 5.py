nome = (input("Escreva o seu nome: "))
idade = int(input("Escreva a sua idade: "))
sexo = (input("Escreva o seu sexo: "))
nota1 = float(input("Escreva a primeira nota: "))
nota2 = float(input("Escreva a segunda nota: "))

total = ((nota1 + nota2 ) / 2)

print (f"Seu nome é: {nome} \nSua idade é: {idade}\nSeu sexo é: {sexo}\nSua primeira nota é: {nota1}\nSua segunda nota é: {nota2}\nA média de suas notas são: {total}")