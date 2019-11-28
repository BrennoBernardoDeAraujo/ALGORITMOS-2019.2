"""
7. Faça um programa que leia e monte dois vetores de números inteiros com 20 números cada. Depois de montados gere um terceiro vetor formado pela diferença dos dois vetores lidos, um quarto vetor formado pela soma dos dois vetores lidos e por último um quinto vetor formado pela multiplicação dos dois vetores lidos."""

vetor1 = [0] * 4
vetor2 = [0] * 4
vetor3 = [0] * 4
vetor4 = [0] * 4
vetor5 = [0] * 4

# Vetor 1
print()
print('Digite os números do primeiro vetor!')
print()
for p in range(4):
    vetor1[p] = int(input(f'Digite {p + 1} números: '))

# Vetor 2
print()
print('Digite os números do segundo vetor!')
print()
for s in range(4):
    vetor2[s] = int(input(f'Digite {s + 1} números: '))

# Vetor 3
for t in range(4):
    vetor3[t] = vetor1[t] - vetor2[t]

# Vetor 4
for q in range(4):
    vetor4[q] = vetor1[q] + vetor2[q]

# Vetor 5
for j in range(4):
    vetor5[j] = vetor1[j] * vetor2[j]

print()
print('----------------------')
print('Resultado')
print()
print(
    f'Vetor1 {vetor1}, \nVetor2 {vetor2}, \nVetor3 {vetor3}, \nVetor4 {vetor4}, \nVetor5 {vetor5}')
