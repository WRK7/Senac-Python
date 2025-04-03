#-------------------TUPLA--------------------

#Tulplas funcionam iguais a listas, mas elas são imutaveis
#podem ser concatenadas

'''li =[2,4,5,6,7]
print (type(li))
li=tuple(li)
print (type(li))
#você pode transformar uma lista em tupla usando o comando tu=tuple(u)
tu = (8,9,10,11,12)
print (type(tu))
tu= list(tu)
print(type(tu))'''

#você pode transformar uma tupla em lista usando tu=list(tu)

#-------------------TESTES CONDICIONAIS--------------------

# se inicia com "if", colocamos a condição e abrimos com dois pontos ao invés da chave
# a identação é feita com os códigos com quatro passos no ínicio (ou com o tab), quando sem esses epaços, o maqinario para


'''age = int(input("Digite a sua idade: "))

if (age>17):
    print ("Vocè é maior de idade. Ja pode dirigir")
else: 
    print("Você é menor de idade, não pode dirigir")
print ("Fim. Dora do if")'''

'''idade = int(input("Digite a sua idade: "))

if (idade >= 16 and idade < 18):
    print ("Você já pode votar")

elif (idade >= 18):
    print ("Você já pode Dirigir e votar")
else: 
    if (idade < 16):
            print ("Apenas continue a estudar")'''