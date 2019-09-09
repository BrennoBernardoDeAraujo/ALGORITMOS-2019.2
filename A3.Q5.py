# Faça um programa que leia 10 números e informe o maior número.

maior = 0
for n in (1,11):
    numero = float(input("Digite um número: "))
    if n == 1:
        maior = numero
    else: 
        if numero > maior:
         maior = numero


print("o maior número é:",maior)