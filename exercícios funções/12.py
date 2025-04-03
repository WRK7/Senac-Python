def palindromo(s):
    revertido=''
    cont =0
    for i in range ((len(s)-1),-1,-1):
       revertido+= s[i]
    for i in range(0, len(s)):
        if(s[i] == revertido[i]):
            cont = cont+1
    if(len(s) == cont):
        return 'palindromo'
    else:
        return 'não palindromo'


print(palindromo('paquipapigrafo'))

# josé que ensinou (e eu ainda não entendi)