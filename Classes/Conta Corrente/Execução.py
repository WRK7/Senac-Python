from Conta_corrente import Conta_Corrente

conta_corrente1 = Conta_Corrente(12,"Wesker",0)
print (conta_corrente1.MostrarNome())
conta_corrente1.AlterarNomes()
print (conta_corrente1.MostrarNome())
conta_corrente1.Deposito()
conta_corrente1.Saque()