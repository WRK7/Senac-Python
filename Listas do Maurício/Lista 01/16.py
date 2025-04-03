def retira_espacos(texto):
    textos=''
    lista = texto.split()
    for i in range(0, len(lista)):
        textos += lista[i]
    return textos
    
print(retira_espacos('Lorem Ipsun Lorem Ipsun Lorem Ipsun Lorem Ipsun Lorem Ipsun Lorem Ipsun Lorem Ipsun Lorem Ipsun Lorem Ipsun' ))

# josé que ensinou (e eu ainda não entendi)