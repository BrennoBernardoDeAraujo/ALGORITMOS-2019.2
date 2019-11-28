"""
Aluno: Luan dos Santos Rodrigues
Matricula: 192810286
Curso: Bacharelado em Computação - UEPB
Cadeira: Algoritmos 2019.2
Turno: Manhã
Prof. Ricardo Oliveria 

10. Faça um programa que leia um vetor de 10 posições e verifique se existem valores repetidos e os escreva na tela.
"""

vetor = [0]*10
aux = []

for i in range(10):
    vetor[i] = int(input('Digite o valor: '))

for i in range(10):
    for j in range(i):
        if vetor[j] == vetor[i]:
            aux = aux + [vetor[i]]
print(f'Números repetidos são: {aux}')
