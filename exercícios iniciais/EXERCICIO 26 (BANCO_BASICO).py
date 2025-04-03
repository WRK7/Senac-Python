senha = 00
senha1 = int(input("Digite a senha: "))
decisao = 0
extrato = 0
lista = [00.00]
listanome = []
listacpf = []
listafone = []
listasexo = []
while (decisao != "5"):
    if ( senha1 != senha):
        print ("senha invalida!")
    elif (senha1 == senha):
        print ("=================Banco não suspeito================")
        print ("Bem vindo Usuario")
        print ("1", " - Extrato")
        print ("2", " - Deposito")
        print ("3", " - Saque")
        print ("4", " - ADM")
        print ("5", " - Sair")
        acesso = (input("O que deseja acessar? "))
        if (acesso == "1"):
            print ("=================Extrato================")
            print (f"Você tem R$ {lista} na conta")
        elif (acesso == "2"):
            print ("=================Deposito================")
            deposito = float(input("Digite a quantidade que você quer adicionar: "))
            extrato = (extrato + deposito)
            lista[0] = extrato
            print (f"Foi adicionado um valor de R${lista} em sua conta")
            print (f"Você tem R${lista} em sua conta")
        elif (acesso == "3"):
            print ("=================Saque================")
            print (f"Você tem R${lista} em sua conta")
            saque = float(input("Quanto você quer sacar de sua conta? "))
            if (extrato - saque<0):
                print("Você não saldo o suficiente para fazer esse saque")
            else:
                extrato = extrato - saque
                lista[0] = extrato
            print (f"Foi sacado um valor de R$ {saque} em sua conta")
            print (f"Você tem R${lista} em sua conta")
        if (acesso == "4"):
            print ("1", " - Cadastro")
            print ("2", " - Editar perfil")
            escolha = (input ("Digite uma opção: "))
            if (escolha == "1"):
                nome = (input("Digite o seu nome: "))
                
                cpf = int(input("Digite o seu CPF: "))
                
                fone = int(input("Digite o seu telefone: "))
                
                sexo = (input("Digite o seu sexo: "))
                listanome=nome
                listacpf=cpf
                listafone=fone
                listasexo=sexo
                print ("CADASTRO CONCLUIDO COM SUCESSO\nTe redirecionando para a tela inicial...")
            if (escolha == "2"):
                print("Seus dados atuais")
                print(listanome)
                print(listacpf)
                print(listafone)
                print(listasexo)
                nome = (input("Digite o seu nome: "))
                cpf = int(input("Digite o seu CPF: "))
                fone = int(input("Digite o seu telefone: "))
                sexo = (input("Digite o seu sexo: "))
                listanome=nome
                listacpf=cpf
                listafone=fone
                listasexo=sexo
                print ("EDIÇÃO CONCLUIDA COM SUCESSO\nTe redirecionando para a tela inicial...")
        elif (acesso == "5"):
            print ("Saindo...")