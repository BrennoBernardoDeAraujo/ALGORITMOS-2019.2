"""
6. Leia uma matriz de ordem n, informada pelo usuário.
Calcule a soma dos elementos que estão abaixo da diagonal principal. """

matriz = []
ordem = int(input('Digite a ordem da matriz: '))

for i in range(ordem):
    matriz.append([0]*ordem)

for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = int(input(f'M [{str(i+1)}] [{str(j+i)}]'))

for i in range(ordem):
    for j in range(ordem):
        print(f'[{matriz[i][j]}]', end='')
    print()

soma_diagonal = 0
for i in range(ordem):
    for j in range(ordem):
        if i > j:
            soma_diagonal = soma_diagonal + matriz[i][j]
print(f'Soma dos elementos abaixo da diagonal principal é: {soma_diagonal}')
