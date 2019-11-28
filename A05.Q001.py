'''
A05.Q001 - Faça um programa que possua uma lista denominada A que armazene 6 números intei- ´ ros. O programa deve executar os seguintes passos: 
Atribua os seguintes valores a essa lista: 1, 0, 5, -2, -5, 7. 
Armazene em uma variável inteira (simples) a soma entre os valores das posições A[0], A[1] e A[5] da lista e mostre na tela esta soma. 
Modifique a lista na posição 4, atribuindo a esta posição o valor 100. 
Mostre na tela cada valor da lista A, um em cada linha. '''

A = [1,0,5,-2,-5,7]
print()
soma = A[0] + A[1] + A[5] 
print('a soma entre os valores das posições A[0], A[1] e A[5] da lista é: ',soma)
print()
A[4] = 100

for i in range(6):
    print(A[i])


