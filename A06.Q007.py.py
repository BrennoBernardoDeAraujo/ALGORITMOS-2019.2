"""
A06.Q007 - Leia uma matriz de ordem n, informada pelo usuário. Calcule a soma dos elementos que estão na diagonal secundária. """

ordem = int(input('Digite a ordem da matriz: '))
matriz = []
soma = 0
aux = ordem-1

for i in range(ordem):
    matriz.append([0]*ordem)

for i in range(ordem):
    for j in range(ordem):
        matriz[i][j] = int(input(f'M [{str(i+1)}] [{str(j+i)}]'))

for i in range(ordem):
    for j in range(ordem):
        print(f'[{matriz[i][j]}]', end='')
    print()

for i in range(ordem):
    soma = soma + matriz[i][j]
    aux = aux - 1
print()

print(f'A soma dos elementos da diagonal secundário é: {soma}')
