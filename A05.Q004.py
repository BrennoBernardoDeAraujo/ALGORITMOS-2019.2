'''
A05.Q004 - Escreva um programa que leia 10 números inteiros e os armazene em um vetor. 
Imprima o vetor, o maior elemento e a posição que ele se encontra. '''

numero = [0]*10

for i in range(10):
    PNreal = i + 1
    numero[i] = int(input(f'digite o de posiçao {PNreal}/10 números: '))

maximo = max(numero)
posicao = numero.index(maximo) + 1
print(
    f'Os numeros digitados são: {numero} e o seu maior numero é: {maximo} e se encontra na posição {posicao}')

# Como em listas do dia-dia nao a posiçao zero coloquei para o usuario apartir da posiçao 1