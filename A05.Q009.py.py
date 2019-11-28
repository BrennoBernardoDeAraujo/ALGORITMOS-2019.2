"""
9. Faça um programa que leia uma quantidade de números determinada pelo usuário e armazene em uma lista. Crie outras duas listas, uma para os valores pares e outra para os ímpares.
"""

quantidade = int(input("Quantos elementos deseja inserir? "))
numeros = [0] * quantidade
pares = []
impares = []

for i in range(quantidade):
    numeros[i] = int(input("Digite os valores: "))
    if numeros[i] % 2 == 0:
        pares += [numeros[i]]
    else:
        impares += [numeros[i]]

print(f'Números pares: {pares} \nNúmeros ímpares {impares}')
