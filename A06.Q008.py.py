"""
A06.Q008 - Faça programa que leia uma matriz 3 x 6 com valores reais.
  a. Imprima a soma de todos os elementos das colunas ímpares.
  b. Imprima a média aritmética dos elementos da segunda e quarta colunas.
  c. Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e
  2.
  d. Imprima a matriz modificada. """

matriz = []
soma_impar = 0
media = 0
aux_soma_1 = 0
aux_soma_2 = 0

for i in range(3):
    matriz.append([0]*6)

for i in range(3):
    for j in range(6):
        matriz[i][j] = float(input(
            f'Digite o valor da linha da matriz [{str(i+1)}] e a coluna [{str(j+i)}]: '))

print()
print('Matriz')
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print()

print()

for i in range(3):
    for j in range(6):
        if (j+1) % 2 != 0:
            soma_impar = soma_impar + matriz[i][j]
print(f'A soma dos elementos das colunas ímpares é igual a: {soma_impar}')

for i in range(3):
    aux_soma_1 = aux_soma_1 + matriz[i][j]
    aux_soma_2 = aux_soma_2 + matriz[i][j]

media = (aux_soma_2 + aux_soma_1) / 6
print(f'A média aritimética dos elementos da 2ª e 4ª coluna: {media} ')

for i in range(3):
    matriz[i][5] = matriz[i][0] + matriz[i][1]

print('Matriz alterada:')
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print()
