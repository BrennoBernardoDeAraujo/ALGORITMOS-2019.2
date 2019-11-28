"""
6. Ler um vetor de 10 elementos. Crie um segundo vetor, com todos os elementos na ordem inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim por diante. Imprima os dois vetores."""

vetor = [0]*10
vetor2 = [0]*10

for i in range(10):
    vetor[i] = int(input('Digite 10 números: '))
    vetor3 = 10-i
    vetor2[vetor3 - 1] = vetor[i]

print(vetor, vetor2)
