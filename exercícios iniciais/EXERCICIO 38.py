# produtos = []

# while True:
#     escolha = int(input("Digite 0 para cancelar e 1 para adicionar mais 1 para adicionar mais um produto: "))

#     if escolha != 0:
#         a = float(input("Digite o valor do produto: "))
#         produtos.append(a)
#     else:
#         break
# dinheiro = float(input("valor do quanto você vai pagar: "))
# sum(produtos)
# print (produtos)



# O código acima é um que eu tentei fazer e deu errado. O código abaixo é a melhora do anterior, depois de eu ter estudado um pouco.

produtos = [0]
nomes = []
escolha3 = 4
break1 = 0
break2 = 0
break3 = 0
break4 = 0
while break1 == 0:
    escolha = int(input("Digite 0 para cancelar e 1 para adicionar um produto: "))
    while break2 == 0:
        if escolha == 1:
            nomes_produto = (input("Digite o nome do produto: "))
            nomes.append(nomes_produto)
            valor_produto = float(input("Agora digite o valor do produto: "))
            if valor_produto <= 0:
                print("Não temos nenhum produto gratuito ou de valor negativo. Tente de novo!")
                produtos = [0]
                nomes = []
                continue
            else:    
                produtos.append(valor_produto)
                escolha2 = int(input("Digite '1' para adicionar outro produto, ou '2' para continuar para o pagamento: "))
                break2 == 1
                if valor_produto > 0:
                    if escolha2 == 2:
                        while break4 == 0:
                            while break3 == 0:
                                if break3 == 0:
                                    dinheiro = float(input("valor do quanto você vai pagar: "))
                                    total_compra = sum(produtos)
                                    if dinheiro >= total_compra:
                                        print(f"Seus produtos são {nomes}")
                                        print (f"O valor da sua compra é de R${total_compra}")
                                        print (f"A quantidade que você ira usar para pagar é de R${dinheiro}")
                                        print (f"Seu troco é de R$", dinheiro-total_compra)
                                        break1 = 1
                                        break2 = 1
                                        break3 = 1
                                        break4 = 1
                                    elif dinheiro < total_compra:
                                        print("Você não tem dinheiro o suficiente para pagar essa compra!")
                                        escolha3 = int(input("Você deseja passar outro valor ou comprar de novo?\nDigite '3' para passar outro valor ou '4' para comprar de novo: "))
                                        if escolha3 == 4:
                                            produtos = [0]
                                            nomes = []
                                            break1 = 0
                                            break2 = 1
                                            break3 = 1
                                            break4 = 1
                            else:
                                continue
        else:
            break
    else:
        break
    break
break1 = 1
