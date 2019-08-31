# 6.Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input("digite um numero: "))
n2 = float(input("digite outro numero: "))
n3 = float(input("digite mais outro numero: "))

if n1 <= n2 and n2 <= n3:
    print(n3,n2,n1)
    if n2 < n1:
        aux = n1
        n1 = n2
        n3 = aux
    if n3 < n2:
        aux = n3
        n3 = n2
        n2 = aux
    if n3 < n2:
        aux = n3
        n3 = n2
        n2 = aux
    if n2 < n1:
        aux = n1
        n1 = n2
        n2 = aux
print("Os numeros em ordem decrescente: ",n3,n2,n1)