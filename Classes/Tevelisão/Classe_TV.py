class Tv:
    def __init__ (self,Canal,Volume):
        self.Canal = ['SBT','GLOBO','RECORD','CARTOONNETWORK','NICKELODEON','PICA-PAU','SONIC','JOSÉARNALDO']
        self.Volume = 0
        self.contador1 = 0
    def MudarCanal (self,botao):
        if botao=='>':
            self.contador1 +=1
            if self.contador1 > 3:
                self.contador1 = 0
            laranja = self.Canal[self.contador1]
            print (laranja)
        elif botao=='<':
            self.contador1 -=1
            if self.contador1 < 0:
                self.contador1 = 0
            laranja = self.Canal[self.contador1]
            print (laranja)
        else: 
            print("Valor invalido")
            raise SystemExit("Programa encerrado!")

            
    def MudarVolume (self,botaovolume):
        if botaovolume=='+':
            self.Volume +=1
            if self.Volume >= 0 and self.Volume < 100:
                laranja = self.Volume
                print (laranja)
            else:
                print("Volume inexistente")
                raise SystemExit("Programa encerrado!")

                
        elif botaovolume=='-':
            self.Volume -=1
            if self.Volume >= 0 and self.Volume < 100:
                laranja = self.Volume
                print (laranja)
            else:
                print ("Volume inexistente")
                raise SystemExit("Programa encerrado!")
        else: 
            print("Valor invalido")
            raise SystemExit("Programa encerrado!")

            
