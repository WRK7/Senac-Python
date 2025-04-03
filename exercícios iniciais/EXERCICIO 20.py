# Janeiro = print (float(input("Tmeperatura média de Janeiro")))
# Fervereiro = print (input("Tmeperatura média de Fevereiro"))
# Março = print (input("Tmeperatura média de Março"))
# Maio = print (input("Tmeperatura média de Maio"))
# Abril = print (input("Tmeperatura média de Abril"))
# Junho = print (input("Tmeperatura média de Junho"))
# Julho = print (input("Tmeperatura média de Julho"))
# Agosto = print (input("Tmeperatura média de Agosto"))
# Setembro = print (input("Tmeperatura média de Setembro"))
# Outubro = print (input("Tmeperatura média de Outubro"))
# Novembro = print (float(input("Tmeperatura média de Novembro")))
# Dezembro = print (float(input("Tmeperatura média de Dezembro")))



#=======================================================================

#Faça um programa que contenha duas temperaturas por mÊs, uma em cada lista de todos os meses do ano. Após isso, calcule a média anual das temperaturas, mostre a maior e a menor. imprimir em ordem crescente. não utilizar as mesmas temperaturas.

lista = []

ja=[34,22]
fe = [22,34]
mar = [22,55]
mai = [33,12]
abr = [15,22]
jun = [35,12]
jul = [43,11]
ago = [23,33]
sete = [33,11]
out = [11,22]
nov = [10,4]
dez = [76,5]

lista.extend (ja)
lista.extend (fe)
lista.extend (mar)
lista.extend (mai)
lista.extend (abr)
lista.extend (jun)
lista.extend (jul)
lista.extend (ago)
lista.extend (sete)
lista.extend (out)
lista.extend (nov)
lista.extend (dez)

print(lista)

lista.sort()

print (lista)

lista.sort(reverse = True)

print (lista)

print (max(lista))
print (min(lista))

print (sum(lista)/24)









