import os

print ("Vamos criar o seu cadastro. Responda as nossas perguntas.")

nome = (input("Digite o seu nome: "))
Cpf = int(input("Digite o seu cpf: "))
Rg = int(input("Digite o seu Rg: "))
data = int(input("Digite a sua data de nascimento: "))
sexo = (input("Digite o seu sexo: "))
peso = float(input("Digite o seu peso: "))
tiposangue = (input("Digite o seu tipo sanguineo: "))
renda = int(input("Digite a sua renda: "))
endereco = (input("Digite o seu endereço: "))
telefone = int(input("Digite o seu telefone: "))
cidade = (input("Digite a sua cidade: "))
estado = (input("Digite o seu estado: "))

os.system('cls')

print (f"Seu nome é: {nome}\nSeu CPF é: {Cpf}\nSeu RG é: {Rg}\nA sua data de nascimento é: {data}\nO seu sexo é: {sexo}\nO seu peso é: {peso}\nO seu tipo sanguineo é: {tiposangue}\nA sua renda é: {renda}\nO seu endereço é: {endereco}\nO sue telefone é: {telefone}\nA sua cidade é: {cidade}\nO seu estado é: {estado}")