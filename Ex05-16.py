from os import system as lp
lp('cls')
a = int(input ("digite um valor que vai representar A "))
b = int(input("digite um valor que vai representar B "))

c = int(input ("digite um valor que vai representar C "))
d = int(input ("digite um valor que vai representar D "))
soma1 = a == b
soma2 = b == d

soma3 = soma1 or soma2  
print (f"Resultado A=B : {soma1} \n Resultado C=D :{soma2}\n valor em or {soma3}")
