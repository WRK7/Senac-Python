def blitz (n):
    soma = 0
    for i in range (0,n):
       soma = (((-1)**i)/(2*i+1) + soma)
    return soma*4

print (blitz(23))