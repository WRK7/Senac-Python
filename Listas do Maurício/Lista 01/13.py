def palindromo(s, letra):
    cont = 0
    for i in range(0, len(s)):
        if(s[i] == letra):
            cont = cont+1
    return cont

print(palindromo('mustang', 'a'))

# josé que ensinou (e eu ainda não entendi)