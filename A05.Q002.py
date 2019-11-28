'''
A05.Q001 -  Ler um conjunto de números reais, armazenando-o em vetor e calcular 
o quadrado das ´ componentes deste vetor, armazenando o resultado em outro vetor. 
Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.'''

lista1 = [0] * 10
lista2 = [0] * 10

for i in range(10):
    lista1 [i] = float(input("Número de posiçao " + str(i + 1) + " do vetor: "))

for i in range(10):
    lista2 [i] = lista1 [i] * lista1 [i]

print()
print("vetor")
print(lista1)
print()
print()
print()
print("Quadrado das componentes do vetor:")
print(lista2)