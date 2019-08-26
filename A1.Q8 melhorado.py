# 8. Faça um programa que leia um valor inteiro e mostre na tela uma sequência incluindo os
# dois números que vem antes, o número digitado, e os dois números que vem depois dele.
# Ex.: digitou 5; o programa mostra 3 4 5 6 7.

N = int(input("Digite um valor inteiro: "))
A1 = int (N - 2)
A2 = int (N - 1)
P1 = int (N + 1)
P2 = int (N + 2)
print (A1,A2,N,P1,P2)

# Siginificado das siglas:

# N = int(input("Digite um valor inteiro: "))
# A1 = Gera o primeiro antecessor 
# A2 = Gera o segundo antecessor
# P1 = Gera o primeiro sucessor
# P2 = Gera o segundo sucessor
# (A1,A2,N,P1,P2) = ordena os ítens